from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.db.models import Count, Sum
from datetime import timedelta
from django.contrib.auth.models import User
from urllib3 import request
from .models import UserProfile, UserAttempt
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress


@login_required
def dashboardView(request):
    """View for the user dashboard page of the site."""
    user = request.user
    attempts = request.user.attempts.all()
    userprofile = request.user.userprofile
    now = timezone.now()

    # Calculate statistics for the user's attempts in specific time frames
    today = now.date()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    attempts = user.attempts.all()

    # Points
    points_today = (
        attempts
        .filter(timestamp__date=today)
        .aggregate(total_points=Sum('points_awarded'))['total_points']
        or 0
    )

    points_week = (
        attempts
        .filter(timestamp__gte=week_ago)
        .aggregate(total_points=Sum('points_awarded'))['total_points']
        or 0
    )

    points_month = (
        attempts
        .filter(timestamp__gte=month_ago)
        .aggregate(total_points=Sum('points_awarded'))['total_points']
        or 0
    )

    # Accuracy
    total_attempts = attempts.count()
    correct_attempts = attempts.filter(is_correct=True).count()

    accuracy = 0
    if total_attempts > 0:
        accuracy = round(correct_attempts / total_attempts * 100, 2)

    context = {
        'userprofile': userprofile,
        'total_attempts': total_attempts,
        'correct_attempts': correct_attempts,
        'points_today': points_today,
        'points_week': points_week,
        'points_month': points_month,
        'accuracy': accuracy,
    }
    return render(request, 'user/dashboard.html', context)


@login_required
def accountProfileView(request):
    """View for the user profile page of the site."""
    user = request.user
    userprofile = request.user.userprofile
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    email = user.email
    subscription_status = "Premium" if userprofile.is_premium else "Free"
    context = {
        'userprofile': userprofile,
        'email': email,
        'username': username,
        'subscription_status': subscription_status,
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, 'user/profile.html', context)


@login_required
def editProfileView(request):
    user = request.user
    userprofile = user.userprofile

    if request.method == 'POST':
        old_email = user.email
        new_email = request.POST.get('email')
        
        if new_email and new_email != old_email:
            user.email = new_email

            userprofile.email_verified = False

            # Clean old emails
            EmailAddress.objects.filter(user=user).exclude(email=new_email).delete()

            # Create/update new email
            email_address, created = EmailAddress.objects.update_or_create(
                user=user,
                email=new_email,
                defaults={'verified': False, 'primary': True},
            )

            email_address.send_confirmation(request)

            messages.info(request, "Please check your email to verify your new address.")

        user.first_name = request.POST.get('first_name') or user.first_name
        user.last_name = request.POST.get('last_name') or user.last_name

        user.save()
        userprofile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('edit_profile')

    return render(request, 'user/edit_profile.html', {
        'userprofile': userprofile
    })


@login_required
def deleteAccountView(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()

        return redirect('home')  

    return render(request, 'user/delete_account.html')