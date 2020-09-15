from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name="show"),
    path('product/', views.add_product, name="add_product"),
    path('add/', views.add_customer, name="add_customer"),
    path('delete/<id>/', views.delete_customer, name="delete_customer"),
    path('delete-product/<id>/', views.delete_product, name="delete_product"),
]