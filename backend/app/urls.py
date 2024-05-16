
from django.urls import path, include
from .views import *
from . import views


app_name = "app"

urlpatterns = [
    path('', Welcome.as_view(), name="welcome-page"),
    path('home/', Home.as_view(), name="home-page"),
    path('about_us/', AboutUs.as_view(), name="about-us-page"),
    path('contact_us/', ContactUs.as_view(), name="contact-us-page"),  
    path('message/', MessageView.as_view(), name="message-page"),  
    path('contact_us/', ContactUs.as_view(), name="contact-us-page"),  
]