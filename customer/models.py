from django.db import models
from register_login.models import CustomerSeller
from seller.models import Items
    
class Cart(models.Model):
    customer = models.ForeignKey(CustomerSeller, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item.name