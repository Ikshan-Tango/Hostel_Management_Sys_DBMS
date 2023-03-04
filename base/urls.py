#make the urls.py of a django app 

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.AllRoutes.as_view(), name="routes"),
    path("user/",views.User.as_view(), name="users"),
]