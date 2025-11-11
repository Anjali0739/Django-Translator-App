from django.urls import path
from .views import createnotes, getnotes

urlpatterns = [
    path("", createnotes, name="createnotes"),
    path("<int:id>/", getnotes, name="getnotes"),
]
