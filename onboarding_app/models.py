from django.db import models

# Create your models here.
from django.db import models

class Seller(models.Model):

    name_of_store = models.CharField(max_length=100)
    balance = models.IntegerField()
    price = models.IntegerField()
    network = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    

    def __str__(self):
        return self.email
    