from hashlib import blake2s
from django.db import models
from product.models import Product

# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)