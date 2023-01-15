from django.contrib import admin
from artist.models import Artist
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Artist)
class ArtistAdmin(ImportExportModelAdmin):
    list_display = ("nickname", "first_name", "last_name", "bio")
    ordering = ('?',)
    search_fields = ("nickname__startswith", )
    