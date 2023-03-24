from django.shortcuts import render
from seller.models import Items


def home(request):
    context = {
        'items': Items.objects.filter(sold=False)
    }

    return render(request, 'customer/home.html', context)
