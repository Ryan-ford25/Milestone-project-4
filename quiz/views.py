from django.shortcuts import render

from quiz.models import Question

# Create your views here.

def questionView(request):
    """"View for the quiz page of the site."""
    
    return render(request, 'quiz/questions.html')

def homeView(request):
    """"View for the home page of the site."""
    questions = Question.objects.all()
    if not request.user.is_authenticated or not request.user.userprofile.is_premium:
        questions = Question.objects.filter(is_premium=False)

    return render(request, 'quiz/index.html', {'questions': questions})