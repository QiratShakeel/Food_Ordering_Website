from django.shortcuts import render,redirect
from .models import Food_Type,Food_Category
from .forms import FoodTypeForm,FoodCatForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

@login_required(login_url='admin_signin')
def home(request):
        if request.user.is_authenticated:
            user_name = request.user.username
            return render(request,"Admin_App/template/index.html",{'username':user_name})

# admin registration
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
        form = FoodCatForm(request.POST)
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
    form = FoodCatForm(request.POST or None, instance=obj)
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


