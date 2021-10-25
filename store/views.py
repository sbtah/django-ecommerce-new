from django.shortcuts import render
from .models import Category, Product


def categories(request):

    return {
        'categories': Category.objects.all()
    }


def all_products(request):

    products = Product.objects.all()
    number_of_products = products.count()

    return render(request, 'store/home.html',  {

        'products': products,
        'number_of_products': number_of_products,

    })


def product_detail(request, slug):

    product = Product.objects.get(slug=slug)

    return render(request, 'store/product_detail.html', {

        'product': product,

    })
