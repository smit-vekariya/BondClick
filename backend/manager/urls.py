
from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import periodic_task  as periodic_task_view
from .periodic_task import *

app_name = "manager"

router = DefaultRouter()
router.register(r'sys_parameter', SystemParameterView)

urlpatterns = [
    path('', include(router.urls)),
    path('group_permission/', GroupPermissionView.as_view({"get":"get","post":"post"}), name="group_permission"),
    path('user_groups/', GroupPermissionView.as_view({"get":"user_groups"}), name="user_groups"),
    
    # periodic_task.py
    path('create_scheduler/', CreateScheduler.as_view({'post':'create_scheduler'}), name="create_scheduler"),
    path('periodic_task/', PeriodicTaskView.as_view({'get':'list'}), name="periodic_task"),
]