from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('profile/edit/', views.editProfileView, name='edit_profile'),
    path('profile/', views.accountProfileView, name='profile'),
    path('delete_account/', views.deleteAccountView, name='delete_account'),
    path('edit_profile/', views.editProfileView, name='edit_profile'),
    path('edit_profile/change_password/', views.change_password, name='change_password'),
    path('accounts/password/reset/', views.password_reset, name='password_reset'),
]
