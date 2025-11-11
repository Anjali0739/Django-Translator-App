from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def statsview(request):
    user = request.user
    allnotes = user.user_notes.all()
    notes_count = allnotes.count()
    hindi_count = 0
    english_count = 0
    all_translations = 0
    for notes in allnotes:
        translated_notes=notes.translated_to.all()
        if translated_notes:
            translated_notes=translated_notes[0]
            all_translations = all_translations+translated_notes.count
            if notes.language == "English":
                hindi_count +=1
            else:
                english_count +=1

    
    return JsonResponse(
        data={
            "total_number_of_notes": notes_count,
            "count_of_translations_performed": all_translations,
            "breakdown_by_original_language":{
                "english_count": english_count,
                "hindi_count": hindi_count
            }
        }
    )