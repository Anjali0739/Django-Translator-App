from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        obj = User.objects.create_user(username=username, password=password)
        obj.save()
        return JsonResponse(
            data={"message": "user registered successfully"}, status = 202
        )
    else:
        return JsonResponse(
            data={"message": "invalid method"}, status=405
        )