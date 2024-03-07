from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    categ = [
        ('phone','phone'),
        ('computer','computer'),
        ('television','television'),
        ('storage','storage'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    category = models.CharField(max_length=50,choices=categ)
    stock = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    createAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    