from django.shortcuts import render, get_object_or_404
from .models import Categories,Brands,Products,Tags

# Create your views here.

def homepage(request):
    products = Products.objects.filter(homepage=True)
    return render(request, 'index.html',{"products":products})

def productdetail(request, slug):
    product= get_object_or_404(Products,slug=slug)
    return render(request, "product.html",{"product":product})