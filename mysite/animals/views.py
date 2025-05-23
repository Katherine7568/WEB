from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Animal

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animals/animals.html', {'animals': animals})

def animal_detail(request, animal_slug):
    animal = get_object_or_404(Animal, slug=animal_slug)
    context = {
        'animal': animal
        
    }
    return render(request, 'animals/detail.html', context)

def about(request):
    return render(request, 'animals/about.html')

def page_not_found(request, exception):
    return render(request, 'animals/404.html', status=404)

def index(request):
    context = {
        'title': 'Главная',
        'menu': ['Главная', 'Наши питомцы', 'О приюте'],
    }
    return render(request, 'animals/index.html', context)