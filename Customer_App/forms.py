from django import forms
from .models import Cart_Items,Order

class CartItemForm(forms.ModelForm):
    class Meta:
        model = Cart_Items
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
