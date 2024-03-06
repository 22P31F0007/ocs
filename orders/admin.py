# cakestore_project/cakes/views.
from django.contrib import admin
from django.shortcuts import render
from .models import Order

admin.site.register(Order)
   
    