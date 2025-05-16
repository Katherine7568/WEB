from django.urls import path
from . import views
from django.conf.urls.static import static

path('post/<int:post_id>/', views.post_detail, name='post'),

def post_detail(request, post_id):
    return HttpResponse(f"Пост с ID: {post_id}")

urlpatterns = [
    path('', views.index, name='home'),
    path('animals/', views.animals, name='animals'),
    path('about/', views.about, name='about'),
]