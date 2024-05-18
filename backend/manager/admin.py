from django.contrib import admin
from manager.models import ErrorBase, History, PageGroup, AllPermissions, GroupPermission, SystemParameter


# Register your models here.
@admin.register(ErrorBase)
class ErrorBaseAdmin(admin.ModelAdmin):
    list_display = ("class_name","level","message","traceback","created_on")

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'action', 'action_type', 'ip_addr', 'action_on', 'action_by')


@admin.register(PageGroup)
class PageGroupAdmin(admin.ModelAdmin):
    list_display = ('page_name','page_code','page_breadcrumbs')
 

@admin.register(AllPermissions)
class AllPermissionsAdmin(admin.ModelAdmin):
    list_display = ('page_group','act_name', 'act_code')

@admin.register(GroupPermission)
class GroupPermissionAdmin(admin.ModelAdmin):
    list_display = ('group','permissions', 'has_perm')



@admin.register(SystemParameter)
class SystemParameterAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'description')