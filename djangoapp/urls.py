from django.urls import path
from .views import person_enum

urlpatterns = [
    path('person_enum/', person_enum, name='person_enum'),
]
