from django.contrib import admin
from manager.models import ErrorBase, History

# Register your models here.
@admin.register(ErrorBase)
class ErrorBaseAdmin(admin.ModelAdmin):
    list_display = ("class_name","level","message","traceback","created_on")

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'action', 'action_type', 'ip_addr', 'action_on', 'action_by')

