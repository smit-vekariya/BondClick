
from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import periodic_task 

app_name = "manager"

router = DefaultRouter()
router.register(r'sys_parameter', SystemParameterView)

urlpatterns = [
    path('', include(router.urls)),
    path('group_permission/', GroupPermissionView.as_view({"get":"get","post":"post"}), name="group_permission"),
    path('user_groups/', GroupPermissionView.as_view({"get":"user_groups"}), name="user_groups"),
    
    path('periodic_task/',periodic_task.periodic_task, name='periodic_task'),
    path('interval_schedule/',periodic_task.interval_schedule, name='interval_schedule'),
    path('crontab_schedule/',periodic_task.crontab_schedule, name='crontab_schedule'),
]