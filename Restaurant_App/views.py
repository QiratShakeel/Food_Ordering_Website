from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Branch,Food_Item,Restaurant
from .forms import BranchForm, FoodItemForm,RestaurantForm
from Admin_App.models import Food_Category
from django.contrib.auth import logout

def home(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        rest = Restaurant.objects.get(rest_id= rest_id)
        return render(request,"Restaurant_App/template/index.html",{'rest':rest})
    else:
        return redirect(restaurant_signin)

# Restaurant Registration

def restaurant_signup(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant_signin')
    form = RestaurantForm()  
    return render(request,'Restaurant_App/template/signup.html',{'form': form})

def restaurant_signin(request):
    if request.method == "POST":
        email= request.POST.get('rest_email')
        password= request.POST.get('rest_pass')
        try:
            rest = Restaurant.objects.get(rest_email=email,rest_pass=password)
            request.session['rest_id'] = rest.rest_id
            return redirect('index')
        except Restaurant.DoesNotExist:
            # If user is not found, show error message or redirect to login page with error
            return render(request, 'Restaurant_App/template/signin.html', {'error': 'Invalid username or password'})
        # if rest is not None:
        #     return redirect('index')
    return render(request,"Restaurant_App/template/signin.html")

def restaurant_signout(request):
    logout(request)
    return redirect('restaurant_signin')

# Branch CRUDS
def branch_list(request):
    if 'rest_id' in request.session:
        list=Branch.objects.all()
        return render(request,'Restaurant_App/template/branch/branch_list.html',{'list':list})
    else:
        return redirect(restaurant_signin)

def branch_form(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        if request.method == 'POST':
            form = BranchForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('branch_list')
        form = BranchForm()
        return render(request,'Restaurant_App/template/branch/branch_form.html',{'form': form,'rest_id':rest_id})
    else:
        return redirect('restaurant_signin')

def branch_update(request, id):
    if 'rest_id' in request.session:
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
    else:
        return redirect(restaurant_signin)
    
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
    if 'rest_id' in request.session:
        list=Food_Item.objects.all()
        return render(request,'Restaurant_App/template/food_item/food_item_list.html',{'list':list})
    else:
        return redirect(restaurant_signin)
    
def food_item_form(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        if request.method == 'POST':
            form = FoodItemForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('food_item_list')
        form = FoodItemForm()
        return render(request,'Restaurant_App/template/food_item/food_item_form.html',{'form': form,'cat':Food_Category.objects.all(),'rest_id':rest_id})
    else:
        return redirect('restaurant_signin')


def food_item_update(request, id):
    if 'rest_id' in request.session:
        id = int(id)
        try:
            obj = Food_Item.objects.get(food_item_id = id)
        except Food_Item.DoesNotExist:
            return redirect('food_item_list')
        if request.method=="POST":
            form = FoodItemForm(request.POST or None, files=request.FILES,instance=obj)
            if form.is_valid():
                form.save()
                return redirect('food_item_list')
        form = FoodItemForm()
        return render(request, 'Restaurant_App/template/food_item/food_item_update.html', {'form':form,'food_item':obj,'cat':Food_Category.objects.all()})
    else:
        return redirect("restaurant_signin")
    
        

def food_item_delete(request, id):
    id = int(id)
    try:
        obj = Food_Item.objects.get(food_item_id = id)
    except Branch.DoesNotExist:
        return redirect('food_item_list')
    obj.delete()
    return redirect('food_item_list')

