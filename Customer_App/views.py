from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

@login_required(login_url='customer_signin')
def home(request):
    return render(request,"Customer_App/template/index.html")

def restaurant_detail(request):
    return render(request,"Customer_App/template/restaurant_detail.html")

def food_item_detail(request):
    return render(request,"Customer_App/template/Food_Details/food_item_detail.html")

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

