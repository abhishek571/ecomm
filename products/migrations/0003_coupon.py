# Generated by Django 5.0.1 on 2024-02-07 05:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_colorvariant_sizevariant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('coupon_code', models.CharField(max_length=10)),
                ('is_expired', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField(default=100)),
                ('minimum_amount', models.IntegerField(default=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
