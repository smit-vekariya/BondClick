
from django.urls import path
from .views import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "account"
urlpatterns = [
    path('', Welcome.as_view(), name="welcome_page"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('main_menu/', MainMenuView.as_view(), name="main_menu"),

    # bondclick api
    path("registration/", RegisterBondUser.as_view(), name="register_bond_user"),
    path("verify_register/", VerifyRegisterUser.as_view(), name="register_verify"),
    path("login/", LoginBondUser.as_view(), name="login_bond_user"),
    path("verify_login/", VerifyLoginBondUser.as_view(), name="verify_login"),
    path('bond_user_profile/', BondUserProfile.as_view(), name="bond_user_profile"),


]