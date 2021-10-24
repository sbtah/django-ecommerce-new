from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


# Category model.
class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:

        verbose_name_plural = 'Categories'

    # def get_absolute_url(self):
    #     return reverse('store:category-list', args=[self.slug])

    def __str__(self):
        return self.name


# Product model.
class Product(models.Model):

    name = models.CharField(max_length=255)
    producer = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_creator')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product-details', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.name
