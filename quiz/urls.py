from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
]