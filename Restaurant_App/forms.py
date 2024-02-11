from django import forms
from .models import Branch,Food_Item,Restaurant
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        
class FoodItemForm(forms.ModelForm):
    class Meta:
        model = Food_Item
        fields = '__all__'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'