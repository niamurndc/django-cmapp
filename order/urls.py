from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_order, name="show"),
    path('add/', views.add_order, name="add_order"),
    path('delete/<id>/', views.delete_order, name="delete_order"),
]