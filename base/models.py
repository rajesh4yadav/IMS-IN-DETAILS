from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, null = True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=255, default = 'username')
    image = models.ImageField(null = True)
    phone_number = models.IntegerField(null = True)


    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username']


class ProductType(models.Model):
     name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity =  models.IntegerField()
    department = models.ManyToManyField('Department', null= True,  blank=True)
    type  = models.ForeignKey('ProductType', on_delete=models.SET_NULL,  null=True)


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    quantity  = models.IntegerField()
    Price = models.FloatField()
    vendor = models.ForeignKey('Vendor',on_delete=models.SET_NULL, null=True)


class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.CharField(max_length=300)
    
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    phone_number  = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)
    
class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer  = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)

    
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number  = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)







    


