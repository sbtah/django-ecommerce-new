from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all-products'),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
    path('categories/<slug:slug>/', views.category_list, name='category-list'),
]
