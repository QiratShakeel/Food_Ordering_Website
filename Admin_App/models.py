from django.db import models
# from django.core.validators import MaxLengthValidator,MinLengthValidator
# # Create your models here.

# food_type = (
#     ('veg','veg'),
#     ('non veg','non veg'),
# )

class Food_Type(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_type = models.CharField(max_length = 30)
    def __str__(self):
        return self.food_id

class Food_Category(models.Model): 
    food_cat_id = models.AutoField(primary_key=True)
    food_type_fk= models.ForeignKey(Food_Type,on_delete=models.CASCADE)
    food_cat = models.CharField(max_length = 30)
    def __str__(self):
        return str(self.food_cat_id)