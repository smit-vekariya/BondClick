
from django.urls import path
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "qradmin"
urlpatterns = [
    path("user_list/", UserList.as_view(), name="user_list"),
    path("create_qr_batch/", CreateQRBatch.as_view(), name="create_qr_batch")
]