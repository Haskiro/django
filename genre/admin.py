from django.contrib import admin
from genre.models import Genre
# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    ordering = ('?',)
    search_fields = ("title__startswith", )
