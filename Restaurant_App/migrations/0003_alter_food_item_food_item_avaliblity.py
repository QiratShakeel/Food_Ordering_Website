# Generated by Django 5.0.1 on 2024-02-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_App', '0002_food_item_food_item_discount_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_item',
            name='food_item_avaliblity',
            field=models.BooleanField(default=False),
        ),
    ]