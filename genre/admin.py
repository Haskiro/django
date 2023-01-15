from django.contrib import admin
from genre.models import Genre
from import_export.admin import ImportExportModelAdmin
from import_export import resources
class GenreResource(resources.ModelResource): 
    class Meta:
        model = Genre
# Register your models here.
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = ["title", "description"]
    ordering = ('?',)
    search_fields = ("title__startswith", )
    resource_classes = [GenreResource]