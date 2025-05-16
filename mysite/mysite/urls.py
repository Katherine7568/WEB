from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from homepage import views
from homepage import views as homepage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', include('animals.urls')),
    path('about/', homepage_views.about, name='about'),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)