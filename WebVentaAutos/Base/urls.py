from django.urls import path
from .views import *


# Urls

urlpatterns = [
    path("", home, name= "home"),
    path("about/", about, name= "about"),
    path("blog/", blog, name= about),

]