from django.contrib import admin
from authentication.models import User
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(SimpleHistoryAdmin):
    list_display = ["first_name", "last_name", "bio"]
    ordering = ('?',)
    search_fields = ("nickname__startswith", )
    history_list_display = ["changed_fields"]
    
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            if len(delta.changed_fields) == 0:
                return None
            return delta.changed_fields
        return None

    