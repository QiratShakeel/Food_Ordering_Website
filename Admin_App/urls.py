from django.contrib import admin
from django.urls import path
from Admin_App import views
urlpatterns = [
    path('', views.home,name='index'),
    path('form/', views.food_type_form,name='food_type_form'),
] 