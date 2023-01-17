import imp
from django.contrib import admin
from track.models import Track
from artist.models import Artist 
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget
from import_export import resources, fields

class TrackResource(resources.ModelResource): 
    # artist=fields.Field(widget=ManyToManyWidget(Artist, field='nickname'))
    class Meta:
        model = Track
        fields =("id", 'title', "cover", "audio_file", "released_at")
# Register your models here.
@admin.register(Track)
class TrackAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ["title", "released_at"]
    ordering = ('?',)
    list_filter = ['artist']
    search_fields = ("title__startswith", )
    fields = ("title", "audio_file", "cover", "released_at", "artist")
    raw_id_fields = ["artist"]
    resource_classes = [TrackResource]
