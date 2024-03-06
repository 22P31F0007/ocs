# cakestore_project/cakes/views.py
from django.contrib import admin
from django.shortcuts import render
from .models import Cake

admin.site.register(Cake)
   
    