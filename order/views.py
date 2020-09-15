from django.shortcuts import render, redirect
from .models import Order
from customer.models import Customer, Product
# Create your views here.

def show_order(request):
  order = Order.objects.all()
  customer = Customer.objects.all()
  product = Product.objects.all()
  return render(request, 'order.html', {'orders': order, 'customers': customer, 'products': product})

def add_order(request):
  if(request.method == 'POST'):
    quantity = request.POST['quantity']
    payment = request.POST['payment']
    name = request.POST['name']
    product = request.POST['product']

    order = Order.objects.create(name_id=name, product_id=product, quantity=quantity, payment=payment)
    order.save()
    return redirect('/order/')

def delete_order(request, id):
  order = Order.objects.get(id=id)
  order.delete()
  return redirect('/order/')
