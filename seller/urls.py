from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='seller_home'),
    path('add_item/', views.add_item, name='seller_add_item'),
    path('delete_item/<str:item_id>', views.delete_item, name='seller_delete_item'),
]
