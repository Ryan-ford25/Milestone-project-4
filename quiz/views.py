from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Question

# Create your views here.
LETTER_MAP = {1: "A", 2: "B", 3: "C", 4: "D"}


def questionView(request):
    """"View for the quiz page of the site."""
    
    return render(request, 'quiz/questions.html')

def homeView(request):
    """"View for the home page of the site."""
    questions = Question.objects.all()
    if not request.user.is_authenticated or not request.user.userprofile.is_premium:
        questions = Question.objects.filter(is_premium=False)

    return render(request, 'quiz/index.html', {'questions': questions})

def submit_answer(request, question_id):
    if request.method == "POST":
        question = Question.objects.get(id=question_id)
        selected = request.POST.get("answer")  # 'A', 'B', 'C', 'D'
        
        correct_letter = LETTER_MAP[question.correct_choice]  # Convert number to letter
        is_correct = selected == correct_letter

        return JsonResponse({
            "correct": is_correct,
            "correct_answer": correct_letter
        })