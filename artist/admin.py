from django.contrib import admin
from artist.models import Artist
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class ArtistResource(resources.ModelResource): 
    class Meta:
        model = Artist
# Register your models here.
@admin.register(Artist)
class ArtistAdmin(ImportExportModelAdmin):
    list_display = ("nickname", "first_name", "last_name", "bio")
    ordering = ('?',)
    search_fields = ("nickname__startswith", )
    resource_classes = [ArtistResource]
    