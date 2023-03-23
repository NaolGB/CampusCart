from django.db import models
from customer.models import CustomerSeller

class Items(models.Model):
    name = models.CharField(max_length=256, null=False)
    description = models.CharField(max_length=1024)
    price = models.FloatField(default=0.0, null=False)
    sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    seller = models.ForeignKey(CustomerSeller, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name