from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('upgrade/', views.upgrade, name='upgrade'),
    path('create-checkout/<str:plan>/', views.create_checkout, name='create_checkout'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
]