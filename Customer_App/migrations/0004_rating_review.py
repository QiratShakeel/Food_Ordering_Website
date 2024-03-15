# Generated by Django 5.0.1 on 2024-03-15 02:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_App', '0003_delete_customuser'),
        ('Restaurant_App', '0004_restaurant_timings'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating_Review',
            fields=[
                ('rating_review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rest_fk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant_App.restaurant')),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]