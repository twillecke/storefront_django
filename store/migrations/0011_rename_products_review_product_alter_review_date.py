# Generated by Django 4.1.7 on 2023-03-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_orderitem_product_alter_product_collection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='products',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
