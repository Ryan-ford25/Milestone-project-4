from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboardView(request):
    """"View for the user dashboard page of the site."""
    
    return render(request, 'user/dashboard.html')

@login_required
def accountProfileView(request):
    """"View for the user profile page of the site."""
    
    return render(request, 'user/profile.html')