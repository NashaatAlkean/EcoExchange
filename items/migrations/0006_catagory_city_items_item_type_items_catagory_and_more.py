# Generated by Django 5.0.2 on 2024-03-14 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_items_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='item_type',
            field=models.CharField(blank=True, choices=[('Clothing', 'Clothing'), ('Books', 'Books'), ('Toys', 'Toys'), ('Games', 'Games'), ('School Supplies', 'School Supplies'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Pet Supplies', 'Pet Supplies'), ('Medical Supplies', 'Medical Supplies'), ('Seasonal Items', 'Seasonal Items')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='items',
            name='catagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='items.catagory'),
        ),
        migrations.AddField(
            model_name='items',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='items.city'),
        ),
    ]
