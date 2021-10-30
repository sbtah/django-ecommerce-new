from unittest import skip
from django.http import request
from django.http.response import HttpResponse
from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from store.views import all_products


class TestViewResponses(TestCase):

    def setUp(self):
        """
        Setup of testing databse.
        """
        self.c = Client()
        self.user_1 = User.objects.create(username='admin')
        self.category_1 = Category.objects.create(
            name='Suche Baseny', slug='suche-baseny')
        self.data_1 = Product.objects.create(
            name='Basen', producer='meowbaby', description='', category_id=1, created_by_id=1, image='basen', slug='basen', price='309.99')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts.
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test absolute url for product.
        """
        response = self.c.get(
            reverse('store:product-detail', kwargs={'slug': "basen", }))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test absolute url for category.
        """
        response = self.c.get(
            reverse('store:category-detail', kwargs={'slug': "suche-baseny", }))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Tests a html with HttpRequest.
        """
        request = HttpResponse()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
