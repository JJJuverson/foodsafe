from django.contrib import admin
from django.urls import path
from foodSafeNews import views

urlpatterns = [
    path("news/",views.safe_news)
]