from django.urls import path
from store.views import product_list, product_detail, category_detail

app_name = 'store'

urlpatterns = [
    path('', product_list, name='product-list'),
    path('<slug:slug>', product_detail, name='product-detail'),
    path('category/<slug:slug>', category_detail, name='category-detail'),
]
