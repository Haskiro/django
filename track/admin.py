import imp
from django.contrib import admin
from track.models import Track
# Register your models here.
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ["title", "released_at"]
    ordering = ('?',)
    list_filter = ['artist']
    search_fields = ("title__startswith", )
    fields = ("title", "audio_file", "cover", "released_at", "artist")