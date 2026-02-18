from django.shortcuts import render

# Create your views here.

def dashboardView(request):
    """"View for the user dashboard page of the site."""
    
    return render(request, 'user/dashboard.html')

def accountProfileView(request):
    """"View for the user profile page of the site."""
    
    return render(request, 'user/profile.html')