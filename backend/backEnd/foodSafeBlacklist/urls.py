from django.contrib import admin
from django.urls import path
from foodSafeBlacklist import views

urlpatterns = [
    path("blacklist/",views.safe_blacklist)
]