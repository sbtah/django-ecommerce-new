# Generated by Django 4.0 on 2022-01-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
