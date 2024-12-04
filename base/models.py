from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300, default='username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class ProductType(models.Model):
    name = models.CharField(max_length=300)


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    department = models.ManyToManyField('Department')

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    supplier = models.ForeignKey('Supplier',on_delete=models.SET_NULL,null=True)

class Sell(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.ForeignKey('Customers',on_delete=models.SET_NULL,null=True)

class Customers(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    email = models.EmailField()

class Supplier(models.Model):
    name = models.CharField(max_length=300) 
    address = models.CharField(max_length=300)
    email = models.EmailField()
    ceo = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.IntegerField()
