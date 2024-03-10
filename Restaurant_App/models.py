from django.db import models
from Admin_App.models import Food_Category
# Create your models here.
class Restaurant(models.Model): 
    rest_id = models.AutoField(primary_key=True)
    rest_name= models.CharField(max_length = 50)
    rest_owner_name = models.CharField(max_length = 50)
    rest_email = models.CharField(max_length = 50)
    rest_pass = models.CharField(max_length = 50)
    rest_logo_img = models.ImageField(upload_to='Restaurant_Logo_Img')
    rest_banner_img = models.ImageField(upload_to='Restaurant_Banner_Img')
    def __str__(self):
        return str(self.rest_id)
    
class Branch(models.Model): 
    branch_id = models.AutoField(primary_key=True)
    branch_country= models.CharField(max_length = 50)
    branch_city = models.CharField(max_length = 50)
    branch_locality = models.CharField(max_length = 50)
    rest_fk_id = models.ForeignKey(Restaurant, on_delete= models.CASCADE)
    def __str__(self):
        return str(self.branch_id)
    
class Food_Item(models.Model): 
    food_item_id = models.AutoField(primary_key=True)
    food_item_name= models.CharField(max_length = 50)
    food_item_desc= models.CharField(max_length = 150)
    food_item_price = models.FloatField()
    food_item_avaliblity = models.BooleanField(default=False)
    food_cat_fk = models.ForeignKey(Food_Category, on_delete=models.CASCADE)
    food_img = models.ImageField(upload_to='Food_Item_Img')
    rest_fk_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_item_discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return str(self.food_item_id)

class Restaurant_Timings(models.Model): 
    rest_timing_id = models.AutoField(primary_key=True)
    open_timings= models.TimeField()
    closing_timings= models.TimeField()
    rest_fk_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.rest_timing_id)