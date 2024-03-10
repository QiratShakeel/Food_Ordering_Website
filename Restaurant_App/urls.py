from django.urls import path
from Restaurant_App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='index'),
    path('branch/form', views.branch_form,name='branch_form'),
    path('branch/list/', views.branch_list,name='branch_list'),
    path('branch/update/<int:id>', views.branch_update,name='branch_update'),
    path('branch/delete/<int:id>', views.branch_delete),
    path('food_item/form', views.food_item_form,name='food_item_form'),
    path('food_item/list/', views.food_item_list,name='food_item_list'),
    path('food_item/update/<int:id>',views.food_item_update,name="food_item_update"),
    path('food_item/delete/<int:id>', views.food_item_delete),
    path('signup', views.restaurant_signup,name="restaurant_signup"),
    path('signin', views.restaurant_signin,name="restaurant_signin"),
    path('signout', views.restaurant_signout,name="restaurant_signout"),
    path('restaurant_profile', views.restaurant_profile,name="restaurant_profile"),
    path('restaurant_change_password', views.restaurant_change_password,name="restaurant_change_password"),
    path('restaurant_profile_update/<int:id>', views.restaurant_profile_update,name="restaurant_profile_update"),
    path('timing_form', views.timing_form,name="timing_form"),
    path('timing_update/<int:id>', views.timing_update,name="timing_update"),
    path('timing_details/<int:id>', views.timing_details,name="timing_details"),
    path('cart_items_list', views.cart_items_list,name="cart_items_list"),
    path('orders_list', views.orders_list,name="orders_list"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)