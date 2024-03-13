# Generated by Django 5.0.2 on 2024-03-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('descreption', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
