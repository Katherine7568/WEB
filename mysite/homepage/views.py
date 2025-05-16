from django.shortcuts import render
from django.http import Http404, HttpResponse

def home(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def page_not_found(request, exception):
    return render(request, 'homepage/404.html', status=404)

def post_detail(request, post_id):
    if post_id > 100:
        raise Http404("Пост не найден")
    return HttpResponse(f"Пост с ID: {post_id}")

def index(request):
    context = {
        'title': 'Главная',
        'menu': ['Главная', 'Наши питомцы', 'О приюте'],
    }
    return render(request, 'homepage/index.html', context)

