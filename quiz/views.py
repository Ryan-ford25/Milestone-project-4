from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Question
from user.models import UserAttempt

from user.models import UserAttempt
from .models import Question

# Create your views here.
LETTER_MAP = {1: "A", 2: "B", 3: "C", 4: "D"}

def homeView(request):
    """"View for the home page of the site."""
    questions = Question.objects.all()

    if request.user.is_authenticated:
        answered_questions = list(UserAttempt.objects.filter(user=request.user).values_list('question_id', flat=True))
    else:
        answered_questions = []

    context = {
        'questions': questions,
        'answered_questions': answered_questions
    }

    return render(request, 'quiz/index.html', context)

def submit_answer(request, question_id):
    if request.method == "POST":
        question = Question.objects.get(id=question_id)
        selected = request.POST.get("answer")  # 'A', 'B', 'C', 'D'
        
        # Check if the selected answer is correct
        correct_letter = LETTER_MAP[question.correct_choice]  # Convert number to letter
        is_correct = selected == correct_letter

        selected_number = {v: k for k, v in LETTER_MAP.items()}.get(selected)  # Convert letter back to number

        # Points logic
        points = question.points if is_correct else 0

        # Save the attempt
        UserAttempt.objects.update_or_create(
            user=request.user,
            question=question,
            selected_choice=selected_number,
            is_correct=is_correct,
            points_awarded=points
        )


        return JsonResponse({
            "correct": is_correct,
            "correct_answer": correct_letter
        })
