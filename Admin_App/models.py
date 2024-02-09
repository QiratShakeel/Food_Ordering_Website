from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
# # Create your models here.

food_type = (
    ('veg','veg'),
    ('non veg','non veg'),
)

# class Food_Type(models.Model):
 
#     # fields of the model
    # food_id = models.AutoField(primary_key=True)
    # food_type = models.CharField(choices=food_type,max_length = 30)
 
#     # renames the instances of the model with their title name
#     def __str__(self):
#         return str(self.id)

# class Food_Category(models.Model):
 
#     # fields of the model
#     food_id = models.AutoField(primary_key=True)
#     food_type_fk= models.ForeignKey(food_type,on_delete=models.CASCADE)
#     food_cat = models.CharField(choices=food_type,max_length = 30)
 
#     # renames the instances of the model with their title name
#     def __str__(self):
#         return str(self.id)