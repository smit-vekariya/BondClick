
from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "manager"

router = DefaultRouter()
router.register(r'sys_parameter', SystemParameterView)

urlpatterns = [
    path('', include(router.urls)),
    path('group_permission/', GroupPermissionView.as_view({"get":"get","post":"post"}), name="group_permission"),
    path('user_groups/', GroupPermissionView.as_view({"get":"user_groups"}), name="user_groups"),


]