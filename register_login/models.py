from django.db import models



# both customer and seller are registered in this model, makes it easier to assign roles later
# adapts Django's user model for registration in register/login pages on production
class CustomerSeller(models.Model):
    USER_ROLE_CHOICES = [
        ('CR', 'Customer'),
        ('SR', 'Seller')
    ]
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, unique=True)
    pwd = models.IntegerField(null=False)
    role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CR')
    user_uuid = models.CharField(max_length=1024, blank=False)

    def __str__(self) -> str:
        return self.name