from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from .models import CustomerSeller
from django.contrib import messages


def register(request):
    context = {
        "registeration_form": RegistrationForm,
    }

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('register_login_login')
        else:
            messages.add_message(request, messages.INFO, 'Registration failed, please insert unique email and a number password.')


    return render(request, 'register_login/register.html', context)

def login(request):
    context = {
                "login_form": LoginForm
            }
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        email = request.POST['email']
        pwd = request.POST['pwd']

        try:
            user = CustomerSeller.objects.get(email=email)

            if str(getattr(user, 'pwd')) == pwd:
                request.session['member_id'] = getattr(user, 'user_uuid')
                # login success
                if getattr(user, 'role') == 'CR':
                    return redirect('customer_home')
                elif getattr(user, 'role') == 'SR':
                    return redirect('seller_home')
                else:
                    messages.add_message(request, messages.INFO, 'Login failed, please try again.')
            else:
                messages.add_message(request, messages.INFO, 'Email and password do not match')
        except:
            messages.add_message(request, messages.INFO, 'User not found, please register')

        
    return render(request, 'register_login/login.html', context)