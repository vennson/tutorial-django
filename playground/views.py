from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Max, Min, Sum, Avg
from store.models import Product, Customer, Collection, Order, OrderItem


def sayHello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField()
    )
    queryset = Product.objects.annotate(discounted_price=discounted_price)
    return render(
        request,
        'hello.html',
        {
            'name': 'bens',
            'result': list(queryset),
        },
    )
