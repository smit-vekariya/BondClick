
from django.urls import path
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "qrapp"
urlpatterns = [
    path('scan_qr_code/', ScanQRCode.as_view(), name="scan_qr_code"),
]