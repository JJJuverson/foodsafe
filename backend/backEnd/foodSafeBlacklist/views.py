from django.shortcuts import render
from .models import foodSafe_blacklist
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def safe_blacklist(request):
    if request.method =="GET":
        json = serializers.serialize("json",foodSafe_blacklist.objects.all())
        return JsonResponse({"status":0,"data":json})
    else:
        return JsonResponse({"status":1,"message":"error"})
