
from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter


app_name = "app"


urlpatterns = [
    path('', Welcome.as_view(), name="welcome-page"),
    path('home/', Home.as_view({'get': 'list', 'post':'create'}), name="home-page"),
    path('home/<int:pk>/', Home.as_view({'delete': 'destroy','patch':'partial_update'}), name="home-page-detail"),
    path('delete_update_answer/<int:pk>/', Home.as_view({'delete': 'destroy_answer','put':'update_answer'}), name="delete-update-detail"),
    path('about_us/', AboutUs.as_view(), name="about-us-page"),
    path('contact_us/', ContactUs.as_view(), name="contact-us-page"),  
    path('message/', MessageView.as_view(), name="message-page"),  
]