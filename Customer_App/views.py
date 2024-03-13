from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from Restaurant_App.models import Food_Item
from Restaurant_App.forms import FoodItemForm
from Admin_App.models import Food_Category,Food_Type
from django.http import JsonResponse
from math import ceil
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.db import transaction
from .models import Order,Cart_Items
from Restaurant_App.models import Restaurant,Restaurant_Timings
import json
# from django.db.models import Max

@login_required(login_url='customer_signin')    
def home(request):
    if request.user.is_authenticated:
        name = request.user.username
        items = Food_Item.objects.all()
        cat = Food_Category.objects.all()
        type = Food_Type.objects.all()
        restaurant = Restaurant_Timings.objects.all()[:8]
        # max_discount_item = Food_Item.objects.aggregate(max_discount=Max('food_item_discount_price'))
        # max_discount_price = max_discount_item['max_discount']
        # food_item_with_max_discount = Food_Item.objects.filter(food_item_discount_price=max_discount_price).first()
        n = len(items)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allItems = [[items,range(1,len(items)),nSlides]]
        allCat = [[cat,range(1,len(cat)),nSlides]]
        params={'allItems':allItems,'allCat':allCat,"type":type,"restaurant":restaurant,"name":name}
        return render(request,"Customer_App/template/index.html",params)

def restaurant_detail(request,id):
    if request.user.is_authenticated:
        name = request.user.username
        obj=Restaurant.objects.get(rest_id=id)
        allItems=Food_Item.objects.filter(rest_fk_id=id)
        discounted_items = Food_Item.objects.filter(rest_fk_id=id, food_item_discount_price__gt=0).order_by('-food_item_discount_price')[:3]
        printed_categories = set()
        unique_category_food_items = []
        for item in allItems:
            category = item.food_cat_fk.food_cat
            if category not in printed_categories:
                unique_category_food_items.append(item)
                printed_categories.add(category)
        params={"obj":obj,"name":name,"allItems":allItems,"category_food_items":unique_category_food_items,"discounted_items":discounted_items}
        return render(request,"Customer_App/template/restaurant_detail.html",params)

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
        # number=request.POST.get('cust_number')
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

@login_required(login_url='customer_signin')
def checkout(request):
    if request.user.is_authenticated:
        id = int(request.user.id)
        user = User.objects.get(id=id)
        user_fk=int(user.id);      
        if request.method == "POST":
            print("request body is:",request.body)
            user_ki_id=request.POST.get('user_fk')
            userkiID=int(user_ki_id)
            # user_fkID=int(user_fk)
            order_total_price=request.POST.get('order_total_price')
            order_address_city=request.POST.get('order_address_city')
            order_address=request.POST.get('order_address')
            order_address_landmark=request.POST.get('order_address_landmark')
            order_address_instructions=request.POST.get('order_address_instructions')
            print("User id is:",user_fk)
            print("order total price is:",order_total_price)
            print("order city is:",order_address_city)
            print("order address is:",order_address)
            print("order landmark is:",order_address_landmark)
            print("order instructions is:",order_address_instructions)            
            order=Order.objects.create(
                user_fk=user_fk,
                order_total_price=order_total_price,
                order_address_city=order_address_city,
                order_address=order_address,
                order_address_landmark=order_address_landmark,
                order_address_instructions=order_address_instructions 
            )
            print("order is in request.POST body:",order)
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            data=json.loads(request.body)
            key=data.get('key')
            cart=data.get('cart')
            print("request body is from ajax:",request.body)
            print("Ajax data is:",data)
            print("Ajax data key is:",key)
            print("Ajax data cart is:",cart)
            print("order is in request.AJAX body:",order)
            for item in cart:
                print("list is:",item)
                print("list Id is:",item['id'])
                print("list Id is:",item.get('id'))
                print("list Qty is:",item['qty'])
                print("list instructions is:",item['instructions'])                    
                return render(request,"Customer_App/template/checkout.html")
        return render(request,"Customer_App/template/checkout.html",{"user_fk":user_fk})


# @login_required(login_url='customer_signin')
# def checkout(request):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         userId = User.objects.get(id=user_id)
#         try:
#             with transaction.atomic():
#                 if request.is_ajax():  # Checking for AJAX request
#                     data = json.loads(request.body)
#                     key = data.get('key')
#                     if not key:
#                         user_fk = userId
#                         order_total_price = data.get('order_total_price')
#                         order_address_city = data.get('order_address_city')
#                         order_address = data.get('order_address')
#                         order_address_landmark = data.get('order_address_landmark')
#                         order_address_instructions = data.get('order_address_instructions')
#                         order = Order.objects.create(
#                             user_fk=user_fk,
#                             order_total_price=order_total_price,
#                             order_address_city=order_address_city,
#                             order_address=order_address,
#                             order_address_landmark=order_address_landmark,
#                             order_address_instructions=order_address_instructions
#                         )
#                         order.save()
#                     else:
#                         cart = data.get('cart')
#                         for item in cart:
#                             food_item_fk = item.get('id')
#                             cart_item_qty = item.get('qty')
#                             cart_item_instructions = item.get('instructions')
#                             food_item = Food_Item.objects.get(food_item_id=food_item_fk)
#                             price = food_item.food_item_price
#                             cart_item_price = cart_item_qty * price
#                             Cart_Items.objects.create(
#                                 order_fk=order.order_id,
#                                 food_item_fk=food_item_fk,
#                                 cart_item_qty=cart_item_qty,
#                                 cart_item_price=cart_item_price,
#                                 cart_item_instructions=cart_item_instructions
#                             )
#                         return JsonResponse({'success': True})  # Returning JSON response for success
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)  # Returning JSON response for error
#     return render(request, "Customer_App/template/checkout.html")


# profile
def customer_profile(request):
    if request.user.is_authenticated:
        id = request.user.id
        name = request.user.username
        email = request.user.email
        params={"name":name,"email":email,"id":id}
        return render(request,"Customer_App/template/customer_settings/customer_profile.html",params)
    
def customer_change_password(request):
    if request.user.is_authenticated:
            id = request.user.id
            user=User.objects.get(id=id)
            if request.method == "POST":
                current_password = request.POST.get('current_password')
                new_password = request.POST.get('new_password') 
                confirm_new_password = request.POST.get('confirm_new_password')
                if user.check_password(current_password):
                    if new_password == confirm_new_password:
                        user.set_password(new_password)
                        user.save()
                        params={"msg":"password is Changed !!"}
                        return render(request,"Customer_App/template/customer_settings/customer_change_password.html",params)
                    else:
                        params={"msg":"Confirm password is not match to new password !!"}
                        return render(request,"Customer_App/template/customer_settings/customer_change_password.html",params)
                else:
                    params={"msg":"Password doesnt match to the current password !!"}
                    return render(request,"Customer_App/template/customer_settings/customer_change_password.html",params)
    return render(request,"Customer_App/template/customer_settings/customer_change_password.html")

def customer_profile_update(request,id):
    obj=User.objects.get(id=id)
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        obj.username= name
        obj.email= email
        obj.save()
        params={"msg":"Your Profile is Updated!",'id':obj.id,"name":name,"email":email}
        return render(request,"Customer_App/template/customer_settings/customer_profile.html",params)
    return render(request,"Customer_App/template/customer_settings/customer_profile_update.html",{"obj":obj})

def all_restaurants(request):
    restaurant = Restaurant_Timings.objects.all()[:8]
    params={"restaurant":restaurant}
    return render(request,"Customer_App/template/all_restaurants.html",params)

def category_items(request,id):
    id=int(id)
    category_item=Food_Category.objects.get(food_cat_id=id)
    items = Food_Item.objects.filter(food_cat_fk=category_item.food_cat_id)
    params={"category_item":category_item,"items":items}
    if not items.exists():
        msg="No Items Exist in this category"
        params={"category_item":category_item,"msg":msg}
        return render(request,"Customer_App/template/category_items.html",params)
    return render(request,"Customer_App/template/category_items.html",params)

# 


# if not key:
#                             user_fk=userId
#                             order_total_price=request.POST.get('order_total_price')
#                             order_address_city=request.POST.get('order_address_city')
#                             order_address=request.POST.get('order_address')
#                             order_address_landmark=request.POST.get('order_address_landmark') if request.POST.get('order_address_landmark') else None 
#                             order_address_instructions=request.POST.get('order_address_instructions') if request.POST.get('order_address_instructions') else None
#                             order = Order.objects.create(
#                                 user_fk=user_fk,
#                                 order_total_price=order_total_price,
#                                 order_address_city=order_address_city,
#                                 order_address=order_address,
#                                 order_address_landmark=order_address_landmark,
#                                 order_address_instructions=order_address_instructions
#                                 )
#                             order.save()
#                         else:
#                             cart=data.get('cart')
#                             print("Received AJAX data cart:", cart)
#                             for item in cart:
#                                 food_item_fk =  item.get('id')
#                                 cart_item_qty = item.get('qty')
#                                 cart_item_instructions = item.get('instructions') if item.get('instructions') else None
#                                 food_item=Food_Item.objects.get(food_item_id=food_item_fk)
#                                 price=food_item.food_item_price
#                                 cart_item_price = cart_item_qty*price
#                                 Cart_Items.objects.create(
#                                     order_fk= order.order_id,
#                                     food_item_fk= food_item_fk,
#                                     cart_item_qty= cart_item_qty,
#                                     cart_item_price=cart_item_price,
#                                     cart_item_instructions= cart_item_instructions
#                                 )
#                             return redirect('customer_index')