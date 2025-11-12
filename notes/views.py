from django.shortcuts import render
import json
from .models import Notes
from django.http import JsonResponse
from rest_framework.decorators import  permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from .serializer import NotesSerializer
from django.core.cache import cache

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def createnotes(request):
    user = request.user
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        language = data.get("language")
        text = data.get("text")


        notes = Notes.objects.create(title=title, language=language, text=text, user=user)
        notes.save()
        return JsonResponse(
            data={"message": "notes created successfully", "id": notes.id}, status = 201
        )
    elif request.method == "GET":
        # notes = Notes.objects.filter(user=user)
        notes = user.user_notes.all()
        resp = NotesSerializer(notes, many=True)
        return JsonResponse( data=resp.data, status=200, safe=False)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def getnotes(request, id):
    user = request.user
    if request.method == "GET":
        cache_key = f"{user.id}_{id}"
        cached_data = cache.get(cache_key)
        if cached_data:
            cache.set(cache_key, cached_data, timeout=300)
            return JsonResponse(data=cached_data, status=200)

        try:
            note = user.user_notes.get(id=id)
        except:
            return JsonResponse({"error": "Note not found"}, status=404)
        resp =NotesSerializer(note).data
        cache.set(cache_key, resp, timeout=300)
        return JsonResponse(data=resp, status=200)
        
            

    elif request.method == "PUT":
        note = user.user_notes.get(id=id)
        data = json.loads(request.body)
        note.title = data.get('title', note.title)
        note.language = data.get('language', note.language)
        note.text = data.get('text', note.text)
        
        note.save()
        resp = NotesSerializer(note)
        return JsonResponse(data=resp.data, status=200)
    
    elif request.method == "DELETE":
        user.user_notes.get(id=id).delete()
        return JsonResponse(data={"message": f"note {id} deleted successfully"}, status = 200)
    
        

