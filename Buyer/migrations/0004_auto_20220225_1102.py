# Generated by Django 3.1.5 on 2022-02-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0003_cart_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_tb',
            name='contactno',
            field=models.IntegerField(default='no phone'),
        ),
    ]
