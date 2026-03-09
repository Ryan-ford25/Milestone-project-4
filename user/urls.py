from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('profile/edit/', views.editProfileView, name='edit_profile'),
    path('profile/', views.accountProfileView, name='profile'),
]
