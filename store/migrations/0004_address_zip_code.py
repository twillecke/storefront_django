# Generated by Django 4.1.7 on 2023-02-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
