from django.contrib import admin
from django.urls import path
from Restaurant_App import views
urlpatterns = [
    path('', views.home,name='index'),
] 