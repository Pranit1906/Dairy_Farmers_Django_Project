# Generated by Django 5.0.1 on 2024-02-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_rename_payemnt_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default='0'),
        ),
    ]