from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('profile/edit/', views.editProfileView, name='edit_profile'),
    path('profile/', views.accountProfileView, name='profile'),
    path('delete_account/', views.deleteAccountView, name='delete_account'),
    path('edit_profile/', views.editProfileView, name='edit_profile'),
    path('verify_email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
]
