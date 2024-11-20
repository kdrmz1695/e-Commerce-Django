from django.shortcuts import render
from .models import Categories,Brands,Products,Tags

# Create your views here.

def homepage(request):
    products = Products.objects.filter(homepage=True)
    return render(request, 'index.html',{"products":products})
