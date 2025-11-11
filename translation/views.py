from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .utils import translate_text

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tranlate(request, id):
    user=request.user
    note = user.user_notes.get(id=id)
    text = note.text
    source = note.language
    target = "en"
    if source=="English":
        source="en"
        target = "hi"
    else:
        source='hi'

    translated = translate_text(text, source, target)
    return JsonResponse(data={"Text": text, "Translated text":translated}, status=200)
    