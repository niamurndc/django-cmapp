from django.db import models

# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  email = models.CharField(max_length=100, unique=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.name
  

class Product(models.Model):
  title = models.CharField(max_length=200)
  desc = models.CharField(max_length=200)
  price = models.IntegerField()

  def __str__(self):
      return self.title
  
  def getprice(self):
    return self.price