from django.contrib import admin
from artist.models import Artist
# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("nickname", "first_name", "last_name", "bio")
    ordering = ('?',)
    search_fields = ("nickname__startswith", )
    