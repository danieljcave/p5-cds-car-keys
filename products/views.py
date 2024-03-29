from django.shortcuts import render
from .models import Product


def all_products(request):
    """A view to show all car keys, incl sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)