from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from Restaurant_App.models import Food_Item
from Restaurant_App.forms import FoodItemForm
from Admin_App.models import Food_Category
from django.http import JsonResponse
from math import ceil
from django.shortcuts import get_object_or_404
from django.http import HttpRequest

@login_required(login_url='customer_signin')
def home(request):
    items = Food_Item.objects.all()
    cat = Food_Category.objects.all()
    n = len(items)
    nSlides = n//4 + ceil((n/4) - (n//4))
    allItems = [[items,range(1,len(items)),nSlides]]
    params={'allItems':allItems,'cat':cat}
    return render(request,"Customer_App/template/index.html",params)

def restaurant_detail(request):
    return render(request,"Customer_App/template/restaurant_detail.html")

def food_item_detail(request):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        object_id = request.GET.get('object_id')
        # Logic to fetch object details using object_id
        try:
            obj = Food_Item.objects.get(food_item_id = object_id)
            object_details = {
                'name': obj.food_item_name,
                'description': obj.food_item_desc,
                'price':obj.food_item_price,
                'image':obj.food_img.url if obj.food_img else None 
                # Add other fields as needed
            }
            return JsonResponse(object_details)
        except Food_Item.DoesNotExist:
            return JsonResponse({'error': 'Object not found'}, status=404)
    else:
        # Handle invalid requests
        return JsonResponse({'error': 'Invalid request'}, status=400)

def cart(request):
    if request.method == 'GET':
        cart_ids = [int(id) for id in request.GET.getlist('cart_ids[]')] 
        # Assuming YourItemModel is the model representing your items
        items_in_cart = Food_Item.objects.filter(food_item_id__in=cart_ids)  # Query items based on IDs
        # Now you can process the items as required
        # For example, you can serialize them to JSON
        serialized_items = [{'food_item_id': item.food_item_id, 'food_item_name': item.food_item_name, 'food_item_price':item.food_item_price, 'food_img':item.food_img.url if item.food_img else None} for item in items_in_cart]
        return JsonResponse({'items_in_cart': serialized_items})

# customer registration
def customer_signup(request):
    if request.method == 'POST':
        name=request.POST.get('cust_name')
        email=request.POST.get('cust_email')
        password=request.POST.get('cust_pass')
        user= User.objects.create_user(name,email,password)
        user.save()
        return redirect('customer_signin')
    return render(request,"Customer_App/template/sign.html")

def customer_signin(request):
    if request.method == 'POST':
        us= request.POST.get('cust_user')
        ps= request.POST.get('cust_pass')
        user=authenticate(request,username=us,password=ps)
        if user is not None:
            login(request,user)
            return redirect('customer_index')
        else:
            return HttpResponse("Invalid")
    return render(request,"Customer_App/template/login.html")

def customer_signout(request):
    logout(request)
    return redirect('customer_index')

