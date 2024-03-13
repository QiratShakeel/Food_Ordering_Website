from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Branch,Food_Item,Restaurant,Restaurant_Timings
from .forms import BranchForm, FoodItemForm,RestaurantForm
from Admin_App.models import Food_Category
from Customer_App.models import Cart_Items,Order
from django.contrib.auth import logout
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.core.serializers import serialize

def home(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        rest = Restaurant.objects.get(rest_id= rest_id)
        total_revenue = Order.objects.exclude(order_total_price=None).count()
        today = timezone.now().date()
        todays_order_total_price = Order.objects.filter(order_date__date=today)
        todays_total_price=0
        for order in todays_order_total_price:
            todays_total_price+=order.order_total_price
        no_of_orders=Order.objects.all().count()
        today = timezone.now().date()
        todays_orders_count = Order.objects.filter(order_date__date=today).count()
        params={"total_revenue":total_revenue,"todays_total_price":todays_total_price,'rest':rest,"no_of_orders":no_of_orders,"todays_orders_count":todays_orders_count}
        return render(request,"Restaurant_App/template/index.html",params)
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
            form = FoodItemForm(request.POST or None,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('food_item_list')
            # else: 
            #     return HttpResponse("form is not valid")
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

# profile 
def restaurant_profile(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        user = Restaurant.objects.get(rest_id= rest_id)
        params ={"user":user}
        return render(request,"Restaurant_App/template/restaurant_settings/restaurant_profile.html",params)
    else:
        return redirect(restaurant_signin)
    
def restaurant_change_password(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        user = Restaurant.objects.get(rest_id= rest_id)
        # params ={"user":user}
        if request.method == "POST":
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_new_password = request.POST.get('confirm_new_password')
            if current_password == user.rest_pass:
                if new_password == confirm_new_password:
                    user.rest_pass = new_password
                    user.save()
                    param={"msg":"Your Password is Changed !!"}
                    return render(request,"Restaurant_App/template/restaurant_settings/restaurant_change_password.html",param)
                else: 
                    param={"msg":"Confirm Password doesnot match to New Password"}
                    return render(request,"Restaurant_App/template/restaurant_settings/restaurant_change_password.html",param)
            else:
                param={"msg":"Password doesnot match to the Current Password"}
                return render(request,"Restaurant_App/template/restaurant_settings/restaurant_change_password.html",param)
        return render(request,"Restaurant_App/template/restaurant_settings/restaurant_change_password.html")

def restaurant_profile_update(request,id):
    if 'rest_id' in request.session:
        obj=Restaurant.objects.get(rest_id=id)
        if request.method=="POST":
            form= RestaurantForm(request.POST,request.FILES,instance=obj)
            if form.is_valid():
                form.save()
                return redirect(restaurant_profile)
        form= RestaurantForm()
        params={"obj":obj,"form":form}
        return render(request,"Restaurant_App/template/restaurant_settings/restaurant_profile_update.html",params)
    else:
        return redirect(restaurant_signin)
# timings CRUD
def timing_form(request):
    if 'rest_id' in request.session:
        rest_id = request.session['rest_id']
        restId=Restaurant.objects.get(rest_id=rest_id)
        try:
            idExist=Restaurant_Timings.objects.get(rest_fk_id=restId)
            if idExist:
                detail_url = reverse('timing_details', kwargs={'id': idExist.rest_timing_id})
                return redirect(detail_url)
        except Restaurant_Timings.DoesNotExist:
            if request.method == "POST":
                open_timings = request.POST.get('open_timings')
                closing_timings= request.POST.get('closing_timings')
                obj=Restaurant_Timings.objects.create(
                    open_timings = open_timings,
                    closing_timings= closing_timings,
                    rest_fk_id = restId
                    )    
                obj.save()
                detail_url = reverse('timing_details', kwargs={'id': obj.rest_timing_id})
                return redirect(detail_url)
        return render(request,"Restaurant_App/template/restaurant_timings/timing_form.html")
    else:
        return redirect(restaurant_signin)

def timing_update(request,id):
    if 'rest_id' in request.session:
        try:
            obj=Restaurant_Timings.objects.get(rest_timing_id= id)
        except:
            return HttpResponse("Id is not found")
        if request.method == "POST":
            open_timings = request.POST.get('open_timings')
            closing_timings= request.POST.get('closing_timings')
            obj.open_timings = open_timings
            obj.closing_timings = closing_timings
            obj.save()
            detail_url = reverse('timing_details', kwargs={'id': obj.rest_timing_id})
            return redirect(detail_url)
        return render(request,"Restaurant_App/template/restaurant_timings/timing_update.html",{"obj":obj})
    else:
        return redirect(restaurant_signin)
    
def timing_details(request,id):
    if 'rest_id' in request.session:
        # rest_id = request.session['rest_id']
        try:
            obj=Restaurant_Timings.objects.get(rest_timing_id= id)
        except:
            return HttpResponse("Id is not found")
        params={"obj":obj}
        return render(request,"Restaurant_App/template/restaurant_timings/timing_details.html",params)
    else:
        return redirect(restaurant_signin)
    
# list
def cart_items_list(request):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        object_id = request.GET.get('object_id')
        # Logic to fetch object details using object_id
        try:
            cart_items=Cart_Items.objects.filter(order_fk=object_id)
            cart_items_data = list(cart_items.values())
            return JsonResponse(cart_items_data,safe=False)
        except Food_Item.DoesNotExist:
            return JsonResponse({'error': 'Cart Item Not Found for the order'}, status=404)
    else:
        # Handle invalid requests
        return JsonResponse({'error': 'Invalid request'}, status=400)


def orders_list(request):
    obj=Order.objects.all()
    params={"list":obj}
    return render(request,"Restaurant_App/template/list/orders_list.html",params)