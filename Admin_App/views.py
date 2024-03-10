from django.shortcuts import render,redirect
from .models import Food_Type,Food_Category
from .forms import FoodTypeForm,FoodCatForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from Restaurant_App.models import Restaurant
from Customer_App.models import Order,Cart_Items

@login_required(login_url='admin_signin')
def home(request):
        if request.user.is_authenticated:
            user_name = request.user.username
            return render(request,"Admin_App/template/index.html",{'username':user_name})

# admin registration
def admin_signup(request):
    if request.method == 'POST':
        name=request.POST.get('admin_name')
        email=request.POST.get('admin_email')
        password=request.POST.get('admin_pass')
        user= User.objects.create_user(name,email,password)
        user.save()
        return redirect('admin_signin')
    return render(request,"Admin_App/template/admin_signup.html")

def admin_signin(request):
    if request.method == 'POST':
        us= request.POST.get('admin_name')
        ps= request.POST.get('admin_pass')
        # superuser = request.POST.get('superuser')
        user=authenticate(request,username=us,password=ps)
        if user is not None:
            if user.is_superuser == 1:
                login(request,user)
                return redirect('home')
        else:
            return HttpResponse("Invalid")
    return render(request,"Admin_App/template/admin_login.html")

def admin_signout(request):
    logout(request)
    return redirect('admin_signin')

# Food Type CRUDS
@login_required(login_url='admin_signin')
def food_type_list(request):
    list=Food_Type.objects.all()
    return render(request,'Admin_App/template/food_type/food_type_list.html',{'list':list})

@login_required(login_url='admin_signin')
def food_type_form(request):
    if request.method == 'POST':
        form = FoodTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_type_list')
    form = FoodTypeForm()
    return render(request,'Admin_App/template/food_type/food_type_form.html',{'form': form})

@login_required(login_url='admin_signin')
def food_type_update(request, id):
    id = int(id)
    try:
        obj = Food_Type.objects.get(food_id = id)
    except Food_Type.DoesNotExist:
        return redirect('food_type_list')
    form = FoodTypeForm(request.POST or None, instance=obj)
    if form.is_valid():
       form.save()
       return redirect('food_type_list')
    return render(request, 'Admin_App/template/food_type/food_type_update.html', {'form':form,'type':obj})

def food_type_delete(request, id):
    id = int(id)
    try:
        obj = Food_Type.objects.get(food_id = id)
    except Food_Type.DoesNotExist:
        return redirect('food_type_list')
    obj.delete()
    return redirect('food_type_list')

# Food Cat CRUDS
@login_required(login_url='admin_signin')
def food_cat_list(request):
    list=Food_Category.objects.all()
    return render(request,'Admin_App/template/food_cat/food_cat_list.html',{'list':list})

@login_required(login_url='admin_signin')
def food_cat_form(request):
    if request.method == 'POST':
        form = FoodCatForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_cat_list')
    form = FoodCatForm()
    return render(request,'Admin_App/template/food_cat/food_cat_form.html',{'form': form,'type':Food_Type.objects.all()})

@login_required(login_url='admin_signin')
def food_cat_update(request, id):
    id = int(id)
    try:
        obj = Food_Category.objects.get(food_cat_id = id)
    except Food_Category.DoesNotExist:
        return redirect('food_cat_list')
    form = FoodCatForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
       form.save()
       return redirect('food_cat_list')
    return render(request, 'Admin_App/template/food_cat/food_cat_update.html', {'form':form,'type':obj})

def food_cat_delete(request, id):
    id = int(id)
    try:
        obj = Food_Category.objects.get(food_cat_id = id)
    except Food_Category.DoesNotExist:
        return redirect('food_cat_list')
    obj.delete()
    return redirect('food_cat_list')

# profile
def admin_profile(request):
    if request.user.is_authenticated:
            user_name = request.user.username
            email = request.user.email
            id = request.user.id
            params = {"name":user_name,"email":email,"id":id}
            return render(request,"Admin_App/template/admin_settings/admin_profile.html",params)
    
def admin_change_password(request):
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
                        return render(request,"Admin_App/template/admin_settings/admin_change_password.html",params)
                    else:
                        params={"msg":"Confirm password is not match to new password !!"}
                        return render(request,"Admin_App/template/admin_settings/admin_change_password.html",params)
                else:
                    params={"msg":"Password doesnt match to the current password !!"}
                    return render(request,"Admin_App/template/admin_settings/admin_change_password.html",params)
            return render(request,"Admin_App/template/admin_settings/admin_change_password.html")

def admin_update_profile(request,id):
    obj=User.objects.get(id=id)
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        obj.username= name
        obj.email= email
        obj.save()
        params={"msg":"Your Profile is Updated!",'id':obj.id,"name":name,"email":email}
        return render(request,"Admin_App/template/admin_settings/admin_profile.html",params)
    return render(request,"Admin_App/template/admin_settings/admin_update_profile.html",{"obj":obj})

# list
def admin_customers_list(request):
    obj=User.objects.filter(is_superuser=0)
    params={"list":obj}
    return render(request,"Admin_App/template/list/admin_customers_list.html",params)

def admin_restaurants_list(request):
    obj=Restaurant.objects.all()
    params={"list":obj}
    return render(request,"Admin_App/template/list/admin_restaurants_list.html",params)

def admin_orders_list(request):
    obj=Order.objects.all()
    restaurant_name="";
    for order in obj:
        cart_items=Cart_Items.objects.filter(order_fk=order.order_id)
        if cart_items.exists():
            restaurant_name = cart_items.first().food_item_fk.rest_fk_id.rest_name
        else:
            restaurant_name= "N/A" 
    params={"list":obj,"restaurant_name":restaurant_name}
    return render(request,"Admin_App/template/list/admin_orders_list.html",params)