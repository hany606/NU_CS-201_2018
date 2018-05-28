from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.my_view, name='log in '),
    path('loggedin', views.index, name='index')
    ]
