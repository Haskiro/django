from django.contrib import admin
from authentication.models import User
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(SimpleHistoryAdmin):
    list_display = ["first_name", "last_name", "bio"]
    ordering = ('?',)
    search_fields = ("nickname__startswith", )