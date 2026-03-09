
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, Sum
from datetime import timedelta
from django.contrib.auth.models import User
from .models import UserProfile

import user
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

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
    points_today = attempts.filter(timestamp__date=today).aggregate(total_points=Sum('points_awarded'))['total_points'] or 0
    points_week = attempts.filter(timestamp__gte=week_ago).aggregate(total_points=Sum('points_awarded'))['total_points'] or 0
    points_month = attempts.filter(timestamp__gte=month_ago).aggregate(total_points=Sum ('points_awarded'))['total_points'] or 0

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
    """View for the user profile edit page of the site."""
    user = request.user
    userprofile = request.user.userprofile

    if request.method == 'POST':
        # Update user and user profile information based on form data
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        userprofile.save()

    context = {
        'userprofile': userprofile,
    }
    return render(request, 'user/edit_profile.html', context)

@login_required
def dashboardView(request):
    """View for the user dashboard page of the site."""
    user = request.user
    attempts = request.user.attempts.all()
    userprofile = request.user.userprofile

    context = {
        'userprofile': userprofile,
        'attempts': attempts,
    }
    return render(request, 'user/dashboard.html', context)
