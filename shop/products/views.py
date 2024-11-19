from django.shortcuts import render
from .models import Categories,Brands,Products,Tags

# Create your views here.

def homepage(request):
    return render(request, 'index.html')
