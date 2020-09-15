from django.shortcuts import render, redirect
from .models import Customer, Product
# Create your views here.

def show(request):
  customer = Customer.objects.all()
  product = Product.objects.all()
  return render(request, 'index.html', {'customers': customer, 'products': product})

def add_product(request):
  if(request.method == 'POST'):
    title = request.POST['title']
    desc = request.POST['desc']
    price = request.POST['price']

    product = Product.objects.create(title=title, desc=desc, price=price)
    product.save()
    return redirect('/customer/')

def add_customer(request):
  if(request.method == 'POST'):
    name = request.POST['name']
    email = request.POST['email']
    address = request.POST['address']

    customer = Customer.objects.create(name=name, email=email, address=address)
    customer.save()
    return redirect('/customer/')

def delete_product(request, id):
  product = Product.objects.get(id=id)
  product.delete()
  return redirect('/customer/')

def delete_customer(request, id):
  customer = Customer.objects.get(id=id)
  customer.delete()
  return redirect('/customer/')