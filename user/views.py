
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, Sum
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def accountProfileView(request):
    """"View for the user profile page of the site."""
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
    return render(request, 'user/profile.html', context)
