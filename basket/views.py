from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from basket.basket import Basket
from store.models import Product


def basket_summary(request):

    basket = Basket(request)

    return render(request, 'basket/basket-summary.html', {
        'basket': basket,
    })


def basket_add(request):
    """Add items to basket."""
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        response = JsonResponse({
            'test': 'data',
        })
        return response
