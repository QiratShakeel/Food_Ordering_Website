from django.db import models
from django.contrib.auth.models import User
from Restaurant_App.models import Food_Item

# Create your models here.
class Order(models.Model): 
    order_id = models.AutoField(primary_key=True)
    user_fk= models.ForeignKey(User,on_delete=models.CASCADE)
    order_total_price = models.DecimalField(max_digits=7,decimal_places=2)
    order_address_city = models.CharField(max_length = 200)
    order_address = models.CharField(max_length = 300)
    order_address_landmark = models.CharField(max_length = 300)
    order_address_instructions = models.CharField(max_length = 300)
    order_status = models.CharField(max_length = 50,default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_id

class Cart_Items(models.Model): 
    cart_item_id = models.AutoField(primary_key=True)
    order_fk = models.ForeignKey(Order,on_delete=models.CASCADE) 
    food_item_fk= models.ForeignKey(Food_Item,on_delete=models.CASCADE)
    cart_item_qty = models.IntegerField()
    cart_item_price = models.DecimalField(max_digits=7,decimal_places=2)
    cart_item_instructions = models.CharField(max_length = 250)
    def __str__(self):
        return self.cart_item_id
    
