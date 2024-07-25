from django.urls import path, include
from rest_framework.routers import DefaultRouter
from finance.views import *

app_name = "finance"

router = DefaultRouter()
router.register(r'', DashBoardView, basename="dashboard")

urlpatterns = [
    path('', include(router.urls))
]