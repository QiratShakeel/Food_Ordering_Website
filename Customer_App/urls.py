from django.urls import path
from Customer_App import views
urlpatterns = [
    path('', views.home,name='customer_index'),
    path('signup/', views.customer_signup,name='customer_signup'),
    path('signin/', views.customer_signin,name='customer_signin'),
    path('signout/', views.customer_signout,name='customer_signout'),
    path('restaurant_detail/<int:id>', views.restaurant_detail,name='restaurant_detail'),
    path('food_item_detail/', views.food_item_detail,name='food_item_detail'),
    path('cart/', views.cart,name='cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('customer_profile/', views.customer_profile,name='customer_profile'),
    path('customer_profile_update/<int:id>', views.customer_profile_update,name='customer_profile_update'),
    path('customer_change_password/', views.customer_change_password,name='customer_change_password'),
    path('all_restaurants/', views.all_restaurants,name='all_restaurants'),
    path('category_items/<int:id>', views.category_items,name='category_items'),
] 