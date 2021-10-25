from django.test import TestCase
from store.models import Category, Product


class TestCategoryModel(TestCase):

    def setup(self):
        self.data1 = Category.objects.create(name='Basen', slug='basen')

    def test_category_model_entry(self):

        data = self.data1
        self.assertTrue(isinstance(data, Category))
