from django.db import models

# both customer and seller are registered in this model, makes it easier to assign roles later
# adapts Django's user model for registration in register/login pages
class CustomerSeller(models.Model):
    USER_ROLE_CHOICES = [
        ('CR', 'Customer'),
        ('SR', 'Seller')
    ]
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, unique=True)
    role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CR')

    def __str__(self) -> str:
        return self.name
    
class Cart(models.Model):
    customer = models.ForeignKey(CustomerSeller, on_delete=models.CASCADE)
    item = models.ForeignKey('seller.Items', on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item.name