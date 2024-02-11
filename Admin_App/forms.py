from django import forms
from .models import Food_Type,Food_Category
#DataFlair
class FoodTypeForm(forms.ModelForm):
    class Meta:
        model = Food_Type
        fields = '__all__'
        
class FoodCatForm(forms.ModelForm):
    class Meta:
        model = Food_Category
        fields = '__all__'