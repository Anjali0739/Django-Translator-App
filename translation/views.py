from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .utils import translate_text
from .models import Translating

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tranlate(request, id):
    user=request.user
    note = user.user_notes.get(id=id)
    text = note.text
    translated = ""
    try:
        translated_response = note.translated_to.all()[0]
        translated = translated_response.translated_text
        translated_response.count = translated_response.count + 1
        translated_response.save()
    except Exception:
        print("not in cache")

    if translated == "":
        source = note.language
        target = "en"
        if source=="English":
            source="en"
            target = "hi"
        else:
            source='hi'

        translated = translate_text(text, source, target)
        text_translated = Translating.objects.create(note_id=note, translated_text= translated)
    return JsonResponse(data={"Text": text, "Translated text":translated}, status=200)
    