# Generated by Django 5.0.2 on 2024-03-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]