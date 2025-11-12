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
        
        if not username or not password:
            return JsonResponse({"status": "error", "message": "Username and password are required"}, status=400)

        obj = User.objects.create_user(username=username, password=password)
        obj.save()
        return JsonResponse({"status": "success", "message": "User registered successfully"}, status = 201)
    else:
        return JsonResponse({"status": "error", "message": "Invalid HTTP method"}, status=405)