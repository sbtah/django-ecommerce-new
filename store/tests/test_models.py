from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User
from django.urls import reverse


class TestCategoryModel(TestCase):

    def setUp(self):

        self.data1 = Category.objects.create(
            name='Suche Baseny', slug='suche-baseny')

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field attributes."""
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """Test Category model returns."""
        data = self.data1
        self.assertEqual(str(data), 'Suche Baseny')
        self.assertEqual(str(data.slug), 'suche-baseny')

    def test_product_model_absolute_url(self):
        """Test absolute url method of Category model."""
        self.assertEqual(
            self.data1.get_absolute_url(),
            reverse('store:category-detail', args=[self.data1.slug]),
        )


class TestProductModel(TestCase):

    def setUp(self):

        Category.objects.create(
            name='Suche Baseny', slug='suche-baseny')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            name='Basen', producer='meowbaby', description='', category_id=1, created_by_id=1, image='basen', slug='basen', price='309.99')

    def test_product_model_entry(self):
        """Test Category model data insertion/types/field attributes."""
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_product_model_return(self):
        """Test Product model returns."""
        data = self.data1
        self.assertEqual(str(data), 'Basen')
        self.assertEqual(data.producer, 'meowbaby')
        self.assertEqual(data.description, '')
        self.assertEqual(data.category.name, 'Suche Baseny')
        self.assertEqual(data.created_by.username, 'admin')
        self.assertEqual(data.image, 'basen')
        self.assertEqual(data.slug, 'basen')
        self.assertEqual(data.price, '309.99')

    def test_product_model_absolute_url(self):
        """Test absolute url method of Product model."""
        self.assertEqual(
            self.data1.get_absolute_url(),
            reverse('store:product-detail', args=[self.data1.slug]),
        )
