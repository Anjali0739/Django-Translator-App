from django.db import models

# Create your models here.


class Translating(models.Model):
    note_id  = models.ForeignKey("notes.Notes", on_delete=models.CASCADE, related_name="translated_to")
    count = models.IntegerField(default=1)
    translated_text = models.TextField()
