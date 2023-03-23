from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    print(request.session['member_id'])
    return render(request, 'customer/home.html')