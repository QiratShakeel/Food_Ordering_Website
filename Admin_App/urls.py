from django.contrib import admin
from django.urls import path
from Admin_App import views
urlpatterns = [
    path('', views.home,name='home'),
    path('food_type/form', views.food_type_form,name='food_type_form'),
    path('food_type/list/', views.food_type_list,name='food_type_list'),
    path('food_type/update/<int:id>', views.food_type_update,name='food_type_update'),
    path('food_type/delete/<int:id>', views.food_type_delete),
    path('food_cat/form', views.food_cat_form,name='food_cat_form'),
    path('food_cat/list/', views.food_cat_list,name='food_cat_list'),
    path('food_cat/update/<int:id>', views.food_cat_update,name='food_cat_update'),
    path('food_cat/delete/<int:id>', views.food_cat_delete),
    path('signup/', views.admin_signup,name="admin_signup"),
    path('signin/', views.admin_signin,name="admin_signin"),
    path('signout/', views.admin_signout,name="admin_signout"),
    path('admin_profile/', views.admin_profile,name="admin_profile"),
    path('admin_change_password/', views.admin_change_password,name="admin_change_password"),
    path('admin_update_profile/<int:id>', views.admin_update_profile,name="admin_update_profile"),
    path('admin_restaurants_list', views.admin_restaurants_list,name="admin_restaurants_list"),
    path('admin_customers_list', views.admin_customers_list,name="admin_customers_list"),
    path('admin_orders_list', views.admin_orders_list,name="admin_orders_list"),
] 