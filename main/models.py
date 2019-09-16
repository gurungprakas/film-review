from django.db import models
from datetime import datetime


class FilmGenre(models.Model):

    film_genre = models.CharField(max_length=200)
    genre_summary = models.CharField(max_length=200)
    genre_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.film_genre


class FilmSeries(models.Model):
    film_series = models.CharField(max_length=200)

    film_genre = models.ForeignKey(FilmGenre, default=1, verbose_name="Genre", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Film Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.film_series


# Create your models here.
class Films(models.Model):
    film_title = models.CharField(max_length=200)
    film_content_review = models.TextField()
    review_published = models.DateTimeField('date published', default=datetime.now())

    film_series = models.ForeignKey(FilmSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    film_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # otherwise we get "Filmss in admin"
        verbose_name_plural = "Films"

    def __str__(self):
        return self.film_title
