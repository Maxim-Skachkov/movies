from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

from .utils import CommonFields
# Create your models here.


class Category(CommonFields):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Person(CommonFields):
    born = models.DateField("Дата рождения")
    photo = models.ImageField("Фото", upload_to='actors/', blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Актеры и режиссеры'


class Genre(CommonFields):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(CommonFields):
    tagline = models.CharField("Слоган", max_length=100)
    poster = models.ImageField('Постер', upload_to='movies/posters', blank=True)
    year = models.PositiveSmallIntegerField('Год выхода фильма')
    country = models.CharField('Страна', max_length=60)
    actors = models.ManyToManyField(Person, verbose_name='Актеры', related_name='film_actor')
    directors = models.ManyToManyField(Person, verbose_name='Режиссеры', related_name='film_director')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    world_premiere = models.DateField('Премьера в мире')
    budget = models.PositiveIntegerField('Бюджет фильма', help_text="Сумма в USD")
    fees_in_USA = models.PositiveIntegerField('Сборы в США', help_text="Сумма в USD")
    fees_in_words = models.PositiveIntegerField("Сборы в мире", help_text="Сумма в USD")
    film_category = models.ForeignKey(Category, null=True, verbose_name='Категория фильма',
                                 on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.url})
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(CommonFields):
    image = models.ImageField('Кадр из фильма', upload_to='movie_shots/', blank=True)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.SmallIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    user = models.ForeignKey(User, default='deleted_user', on_delete=models.SET_DEFAULT)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    otzyv = models.ForeignKey('Review', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):
    user = models.ForeignKey(User, default="deleter_user", on_delete=models.SET_DEFAULT)
    film_review = models.TextField('Текст отзыва')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Отзыв {self.user} на фильм {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'









