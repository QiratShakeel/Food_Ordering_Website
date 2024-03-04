from django.urls import path
from Customer_App import views
urlpatterns = [
    path('', views.home,name='customer_index'),
    path('signup/', views.customer_signup,name='customer_signup'),
    path('signin/', views.customer_signin,name='customer_signin'),
    path('signout/', views.customer_signout,name='customer_signout'),
    path('restaurant_detail/', views.restaurant_detail,name='restaurant_detail'),
    path('food_item_detail/', views.food_item_detail,name='food_item_detail'),
    path('cart/', views.cart,name='cart'),
] 