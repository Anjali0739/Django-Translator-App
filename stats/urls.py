from django.urls import path
from .views import statsview
urlpatterns = [
    path("", statsview, name="statsview"),
    
]