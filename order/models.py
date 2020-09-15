from django.db import models
from customer.models import Customer, Product
# Create your models here.

class Order(models.Model):
  name = models.ForeignKey(Customer, default=None, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  payment = models.CharField(max_length=20, default='Cash')
  time = models.DateTimeField(auto_now_add=True)


  

  
  

