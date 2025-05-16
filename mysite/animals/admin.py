from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'status')  # Какие поля показывать в списке
    search_fields = ('name', 'breed')  # Поиск по этим полям
    list_filter = ('status',)  # Фильтр справа