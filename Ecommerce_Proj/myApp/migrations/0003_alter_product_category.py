# Generated by Django 5.0.1 on 2024-01-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_product_prodapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CURD', 'Curd'), ('MILK', 'Milk'), ('LASSI', 'Lassi'), ('MILKSHAKE', 'Milkshake'), ('PANEER', 'Paneer'), ('GHEE', 'Ghee'), ('CHEESE', 'Cheese'), ('ICECREAM', 'Ice-Cream')], max_length=15),
        ),
    ]
