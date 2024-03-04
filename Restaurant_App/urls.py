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
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)