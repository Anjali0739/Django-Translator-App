from rest_framework import serializers
from .models import Notes
from user.models import User
from user.serializer import UserSerializer

class NotesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Notes
        fields = ["id", "title", 'language', 'text', "user"]

    