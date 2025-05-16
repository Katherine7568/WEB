from django.shortcuts import render
from .models import Animal

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/list.html', {'animals': animals})

def animal_detail(request, animal_slug):
    return render(request, 'animals/detail.html')