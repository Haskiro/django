from django.contrib import admin
from album.models import Album
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    list_display = ["title", "description"]
    ordering = ('?',)
    search_fields = ("title__startswith", )
    list_filter = ['artist']
