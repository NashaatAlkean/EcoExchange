# Generated by Django 5.0.2 on 2024-03-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_catagory_city_items_item_type_items_catagory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_type',
            field=models.CharField(choices=[('Clothing', 'Clothing'), ('Books', 'Books'), ('Toys', 'Toys'), ('Games', 'Games'), ('School Supplies', 'School Supplies'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Pet Supplies', 'Pet Supplies'), ('Medical Supplies', 'Medical Supplies'), ('Seasonal Items', 'Seasonal Items')], max_length=20, null=True),
        ),
    ]
