from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Customer, Collection, Order, OrderItem

def sayHello(request):
  queryset = Order.objects.select_related(
    'customer').prefetch_related(
    'orderitem_set__product').order_by(
    '-placed_at')[:5]
      
  return render(
    request,
    'hello.html', 
    {
      'name': 'bens', 
      'results': list(queryset),
    },
  )
