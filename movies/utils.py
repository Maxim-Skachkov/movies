from django.db import models


class CommonFields(models.Model):
    name = models.CharField("Имя (название)", max_length=60)
    description = models.TextField('Описание', blank=True)
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name
