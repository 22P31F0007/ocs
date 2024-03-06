# cakestore_project/cakes/views.py
from django.shortcuts import render
from .models import Order

def orderlist(request):
    Orders = Order.objects.all()
    return render(request, 'orders.html', {'Orders': Orders})
   
    
