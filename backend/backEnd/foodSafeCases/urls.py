from django.contrib import admin
from django.urls import path
from foodSafeCases import views

urlpatterns = [
    path("cases/",views.safe_cases)
]