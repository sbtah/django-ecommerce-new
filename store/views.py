from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# This output categories objects to all templates via context manager in settings.
def categories(request):

    return {
        'categories': Category.objects.all(),
        'categories_number': Category.objects.all().count()
    }


def all_products(request):

    products = Product.objects.all()
    number_of_products = products.count()

    return render(request, 'store/home.html',  {

        'products': products,
        'number_of_products': number_of_products,

    })


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug, is_active=True)

    return render(request, 'store/product_detail.html', {

        'product': product,

    })


def category_list(request, slug):

    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/category_list.html', {

        'category': category,
        'products': products,

    })
