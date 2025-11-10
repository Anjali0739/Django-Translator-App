from django.db import models

# Create your models here.

class Notes(models.Model):
    class Lang(models.TextChoices):
        ENGLISH = "english"
        HINDI = "hindi"

    title = models.CharField(max_length=100, null=False)
    language = models.CharField(max_length=50, choices=Lang.choices, default=Lang.ENGLISH)
    text = models.TextField()
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="user_notes")

    def __str__(self):
        return f"{self.id} : {self.title}"
    