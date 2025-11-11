from django.urls import path
from .views import tranlate
urlpatterns = [
    path('<int:id>/', tranlate, name='translate'),

]