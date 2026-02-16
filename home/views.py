from django.shortcuts import render

# Create your views here.

def indexView(request):
    """"View for the home page of the site."""
    
    return render(request, 'home/index.html')