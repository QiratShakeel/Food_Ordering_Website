from django.shortcuts import render


def home(request):
    return render(request,"Restaurant_App/template/index.html")