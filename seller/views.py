from django.shortcuts import render, redirect
from .models import Items
from .forms import ItemsAddForm
from register_login.models import CustomerSeller
from django.contrib import messages

def home(request):
    user = CustomerSeller.objects.get(user_uuid=request.session['member_id'])

    context = {
        'items': Items.objects.filter(seller=user, sold=False)
    }

    return render(request, 'seller/home.html', context)

def add_item(request):
    context = {
        'add_item_form': ItemsAddForm,
        'user_uuid': request.session['member_id']
    }

    if request.method == 'POST':
        # add_item_form = ItemsAddForm(request.POST, request.FILES)
        try:
            user = CustomerSeller.objects.get(user_uuid=request.session['member_id'])

            new_item_form = Items(
                name = request.POST['name'],
                description = request.POST['description'],
                price = request.POST['price'],
                image = request.FILES['image'],
                seller = user
            )

            new_item_form.save()
        except:
            messages.add_message(request, messages.INFO, 'User not found, please login or register')


    return render(request, 'seller/add_item.html', context)

def delete_item(request, item_id):
    Items.objects.get(id=item_id).delete()
    return redirect('seller_home')
