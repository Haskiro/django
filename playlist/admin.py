from django.contrib import admin
from playlist.models import Playlist
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class PlaylistResource(resources.ModelResource): 
    class Meta:
        model = Playlist
# Register your models here.
@admin.register(Playlist)
class PlaylistAdmin(ImportExportModelAdmin):
    list_display = ["title", "description"]
    ordering = ('?',)
    search_fields = ("title__startswith", )
    resource_classes = [PlaylistResource]