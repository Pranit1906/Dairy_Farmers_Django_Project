# Generated by Django 5.0.1 on 2024-01-15 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prodapp',
        ),
    ]
