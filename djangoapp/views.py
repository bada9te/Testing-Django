from django.shortcuts import render
from .models import Person

# Create your views here.
def person_enum(req):
    people = Person.objects.all()
    return render(req, 'person_enum.html', { 'people': people })
