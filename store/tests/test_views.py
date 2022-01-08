from unittest import skip
from django.http.response import HttpResponse
from django.test import TestCase, Client, RequestFactory
from store.models import Category, Product
from django.contrib.auth.models import User
from django.urls import reverse
from store.views import product_list, product_detail


class TestViewResponses(TestCase):

    def setUp(self):
        """
        Setup of testing databse.
        """
        self.c = Client()
        self.factory = RequestFactory()
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

    # This tests a all_product function for title, doctype and status.
    def test_homepage_html(self):
        """
        Tests a homepage with HttpRequest.
        """
        request = HttpResponse()
        response = product_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Zorin | Home</title>', html)
        self.assertTrue(html.startswith('\n<!Doctype html>\n'))
        self.assertEqual(response.status_code, 200)

    # This tests a product_detail function for title, doctype and status.
    def test_product_detail_view(self):
        """
        Test a product detail page with HttpRequests.
        """
        request = HttpResponse()
        response = product_detail(request, slug='basen')
        html = response.content.decode('utf8')
        self.assertIn('<title>Zorin | Basen</title>', html)
        self.assertTrue(html.startswith('\n<!Doctype html>\n'))
        self.assertEqual(response.status_code, 200)

    # Testing all_products view with Request Factory.
    def test_view_function(self):
        """
        Tests a view with Request Factory.
        """
        request = self.factory.get('/product/basen')
        response = product_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Zorin | Home</title>', html)
        self.assertTrue(html.startswith('\n<!Doctype html>\n'))
        self.assertEqual(response.status_code, 200)
