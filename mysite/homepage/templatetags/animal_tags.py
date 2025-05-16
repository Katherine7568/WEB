from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_date():
    return datetime.now().strftime("%d.%m.%Y")

@register.simple_tag
def get_animal_types():
    return [
        {"name": "Кошки", "slug": "cats"},
        {"name": "Собаки", "slug": "dogs"}
    ]

@register.inclusion_tag('homepage/featured_animals.html')
def show_featured_animals():
    featured = [
        {"name": "Барсик", "type": "кот", "age": 2, "image": "homepage/images/cat1.jpg"},
        {"name": "Шарик", "type": "собака", "age": 3, "image": "homepage/images/dog1.jpg"},
    ]
    return {'featured_animals': featured}