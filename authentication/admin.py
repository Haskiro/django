from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import User
from authentication.models import UserFavorite
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html

admin.site.unregister(Group)
admin.site.register(UserFavorite)

# Register your models here.
@admin.register(User)
class UserAdmin(SimpleHistoryAdmin):
    list_display = ["first_name", "last_name", "bio"]
    ordering = ('?',)
    search_fields = ("nickname__startswith", )
    history_list_display = ["changed_fields","list_changes"]
    
    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

    def list_changes(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                fields += str("<strong>{}</strong> changed from <span style='background-color:#ffb5ad'>{}</span> to <span style='background-color:#b3f7ab'>{}</span> . <br/>".format(change.field, change.old, change.new))
            return format_html(fields)
        return None
    