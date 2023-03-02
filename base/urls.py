#make the urls.py of a django app 

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.AllRoutes.as_view(), name="routes"),
    # path("users/",views.MedicineClass.as_view(), name="medicines")
]