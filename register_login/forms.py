from django.db import models
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import CustomerSeller

class RegistrationForm(ModelForm):
    class Meta:
        model = CustomerSeller
        fields = ['name', 'email', 'pwd', 'role']
        labels = {
            'name' : 'User name',
            'email' : 'Email',
            'pwd': 'Password',
            'role': 'Buyer/Seller'
        }

class LoginForm(ModelForm):
    class Meta:
        model = CustomerSeller
        fields = ['email', 'pwd']
        labels = {
            'email' : 'Email',
            'pwd': 'Password',
        }