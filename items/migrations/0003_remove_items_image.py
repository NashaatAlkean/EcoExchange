# Generated by Django 5.0.2 on 2024-03-07 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_items_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='image',
        ),
    ]
