from django.contrib import admin
from .models import Films, FilmGenre, FilmSeries
from tinymce.widgets import TinyMCE
from django.db import models


class FilmAdmin(admin.ModelAdmin):
    # fields = ['film_title',
    #           'review_published',
    #           'film_content']

    fieldsets = [
        ('Title/Date', {'fields':['film_title', 'review_published']}),
        ("URL", {'fields': ["film_slug"]}),
        ("Series", {'fields': ["film_series"]}),
        ('Content', {'fields':['film_content_review']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


admin.site.register(FilmSeries)
admin.site.register(FilmGenre)
admin.site.register(Films, FilmAdmin)
