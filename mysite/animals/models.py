from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Animal.Status.ADOPTED)
class Animal(models.Model):
    class Status(models.IntegerChoices):
        IN_SHELTER = 0, 'В приюте'
        ADOPTED = 1, 'Пристроен'

    name = models.CharField(max_length=100, verbose_name="Кличка")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
    breed = models.CharField(max_length=100, verbose_name="Порода")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    description = models.TextField(verbose_name="Описание", blank=True)
    photo = models.ImageField(
        upload_to='animals/',
        blank=True,
        null=True,
        verbose_name="Фотография",
        default='animals/default.jpg'
    )
    status = models.IntegerField(choices=Status.choices, default=Status.IN_SHELTER, verbose_name="Статус")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата поступления")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    objects = models.Manager()
    published = PublishedManager()
    class Status(models.IntegerChoices):
        IN_SHELTER = 0, 'В приюте'
        ADOPTED = 1, 'Пристроен'
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.IN_SHELTER,
        verbose_name="Статус"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('animal_detail', kwargs={'animal_slug': self.slug})

    @property
    def age_display(self):
        if self.age % 10 == 1 and self.age % 100 != 11:
            return f"{self.age} год"
        elif 2 <= self.age % 10 <= 4 and (self.age % 100 < 10 or self.age % 100 >= 20):
            return f"{self.age} года"
        else:
            return f"{self.age} лет"

    @property
    def status_class(self):
        return 'status-adopted' if self.status == self.Status.ADOPTED else 'status-in-shelter'

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['breed']),
        ]