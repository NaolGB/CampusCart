from django.db import models
from django.forms import ModelForm
from .models import Items

class ItemsAddForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'description', 'price', 'image']
        labels = {
            'name' : 'Item name',
            'description' : 'Description',
            'price': 'Price',
            'image': 'image'
        }