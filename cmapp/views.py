from django.shortcuts import render 
from customer.models import Customer, Product


def index(request):
  customer = Customer.objects.all()
  product = Product.objects.all()
  return render(request, 'index.html', {'customers': customer, 'products': product})