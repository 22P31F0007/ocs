# cakestore_project/cakes/views.py
from django.shortcuts import render
from .models import Cake

def cake_list(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')   
def products(request):
    return render(request,'products.html')
 
    