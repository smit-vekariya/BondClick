
from django.urls import path
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "qradmin"
urlpatterns = [
    path("company_dashboard/", CompanyDashboard.as_view(), name="company_dashboard"),
    path("user_list/", UserList.as_view(), name="user_list"),
    path("qr_batch_list/", QRBatchList.as_view(), name="qr_batch_list"),
    path("qr_code_list/", QRCodeList.as_view(), name="qr_code_list"),
    path("create_qr_batch/", CreateQRBatch.as_view(), name="create_qr_batch")
]