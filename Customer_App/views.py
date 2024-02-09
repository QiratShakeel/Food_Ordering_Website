from django.shortcuts import render
 
def home(request):
    return render(request,"Customer_App/template/index.html")