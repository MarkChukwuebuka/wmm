from django.db import models

# Create your models here.
from django.db import models

class Seller(models.Model):

    name_of_store = models.CharField(max_length=100, default="")
    balance = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    network = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=100, default="")
    
    

    def __str__(self):
        return self.email
    