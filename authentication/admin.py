from django.contrib import admin
from authentication.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "bio"]
    ordering = ('?',)
    search_fields = ("nickname__startswith", )