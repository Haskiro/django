from django.contrib import admin
from playlist.models import Playlist
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Playlist)
class PlaylistAdmin(ImportExportModelAdmin):
    list_display = ["title", "description"]
    ordering = ('?',)
    search_fields = ("title__startswith", )
    