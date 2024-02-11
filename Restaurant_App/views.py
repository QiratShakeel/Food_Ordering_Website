from django.shortcuts import render,redirect
from .models import Branch,Food_Item,Restaurant
from .forms import BranchForm, FoodItemForm,RestaurantForm
from Admin_App.models import Food_Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# @login_required(login_url='signin')
def home(request):
    return render(request,"Restaurant_App/template/index.html")

# Branch CRUDS
def branch_list(request):
    list=Branch.objects.all()
    return render(request,'Restaurant_App/template/branch/branch_list.html',{'list':list})

def branch_form(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BranchForm()
    return render(request,'Restaurant_App/template/branch/branch_form.html',{'form': form})

def branch_update(request, id):
    id = int(id)
    try:
        obj = Branch.objects.get(branch_id = id)
    except Branch.DoesNotExist:
        return redirect('branch_list')
    form = BranchForm(request.POST or None, instance=obj)
    if form.is_valid():
       form.save()
       return redirect('branch_list')
    return render(request, 'Restaurant_App/template/branch/branch_update.html', {'form':form,'branch':obj})

def branch_delete(request, id):
    id = int(id)
    try:
        obj = Branch.objects.get(branch_id = id)
    except Branch.DoesNotExist:
        return redirect('branch_list')
    obj.delete()
    return redirect('branch_list')

# Food Item CRUDS
def food_item_list(request):
    list=Food_Item.objects.all()
    return render(request,'Restaurant_App/template/food_item/food_item_list.html',{'list':list})

def food_item_form(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = FoodItemForm()
    return render(request,'Restaurant_App/template/food_item/food_item_form.html',{'form': form,'cat':Food_Category.objects.all()})

def food_item_update(request, id):
    id = int(id)
    try:
        obj = Food_Item.objects.get(branch_id = id)
    except Food_Item.DoesNotExist:
        return redirect('food_item_list')
    form = FoodItemForm(request.POST or None, instance=obj)
    if form.is_valid():
       form.save()
       return redirect('food_item_list')
    return render(request, 'Restaurant_App/template/food_item/food_item_update.html', {'form':form,'branch':obj,'cat':Food_Category.objects.all()})

def food_item_delete(request, id):
    id = int(id)
    try:
        obj = Food_Item.objects.get(food_item_id = id)
    except Branch.DoesNotExist:
        return redirect('food_item_list')
    obj.delete()
    return redirect('food_item_list')

# Restaurant Registration

def restaurant_signup(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_signin')
    form = RestaurantForm()  
    return render(request,'Restaurant_App/template/signup.html',{'form': form})

def restaurant_signin(request):
    if request.method == "POST":
        email= request.POST.get('rest_email')
        password= request.POST.get('rest_pass')
        rest = Restaurant(rest_email=email,rest_pass=password)
        if rest is not None:
            login(request,rest)
            return redirect('index')
    return render(request,"Restaurant_App/template/signin.html")

def restaurant_signout(request):
    logout(request)
    return redirect('restaurant_signin')
