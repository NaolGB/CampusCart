from django.shortcuts import render
from .models import Items

def home(request):

    return render(request, 'seller/home.html')