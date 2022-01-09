from django.urls import path
from basket.views import basket_summary, basket_add


app_name = 'basket'


urlpatterns = [
    path('', basket_summary, name='basket-summary'),
    path('add/', basket_add, name='basket-add'),
]
