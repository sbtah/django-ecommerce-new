from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request):
    """Lists all active products from db and also counts them."""

    products = Product.products.all()  # Use of custom model manager.
    number_of_products = products.count()

    return render(request, 'store/home.html',  {

        'products': products,
        'number_of_products': number_of_products,

    })


def product_detail(request, slug):
    """Product detail view."""

    product = get_object_or_404(Product, slug=slug, is_active=True)

    return render(request, 'store/product_detail.html', {

        'product': product,

    })


def category_detail(request, slug):
    """Category detail view with all related active products."""

    category = get_object_or_404(Category, slug=slug)
    # This also uses custom model manager.
    products = Product.products.filter(category=category)

    return render(request, 'store/category_detail.html', {

        'category': category,
        'products': products,

    })
