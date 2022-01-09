from django.urls import path
from basket.views import basket_summary


app_name = 'basket'


urlpatterns = [
    path('', basket_summary, name='basket-summary'),
]
