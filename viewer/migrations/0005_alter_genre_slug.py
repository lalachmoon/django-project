# Generated by Django 4.2 on 2024-11-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]