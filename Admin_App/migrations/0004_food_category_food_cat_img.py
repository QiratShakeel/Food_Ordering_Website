# Generated by Django 5.0.1 on 2024-02-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0003_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_category',
            name='food_cat_img',
            field=models.ImageField(default=None, upload_to='Food_Category_Imge'),
        ),
    ]