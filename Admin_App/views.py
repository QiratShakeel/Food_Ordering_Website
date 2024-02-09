from django.shortcuts import render


def home(request):
    return render(request,"Admin_App/template/index.html")
def food_type_form(request):
    return render(request,"Admin_App/template/food_type_form.html")
