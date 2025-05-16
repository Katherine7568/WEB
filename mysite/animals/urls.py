from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('<slug:animal_slug>/', views.animal_detail, name='animal_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)