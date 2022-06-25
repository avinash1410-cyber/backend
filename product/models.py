from django.db import models

# Create your models here.
class Product(models.Model):
    brand=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(blank=True,null=True)
    item=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.item