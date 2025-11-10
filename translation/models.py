from django.db import models

# Create your models here.

class Translating(models.Model):
    note_id  = models.ForeignKey("notes.Notes", on_delete=models.CASCADE, related_name="translated_to")
    eng_count = models.IntegerField(default=0)
    hin_count = models.IntegerField(default=0)

    @property
    def total_tranlations(self):
        return self.eng_count+self.hin_count