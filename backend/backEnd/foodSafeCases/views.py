
from django.shortcuts import render
from .models import foodSafe_cases
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def safe_cases(request):
    if request.method =="GET":
        json = serializers.serialize("json",foodSafe_cases.objects.all())
        return JsonResponse({"status":0,"data":json})
    else:
        return JsonResponse({"status":1,"message":"error"})


