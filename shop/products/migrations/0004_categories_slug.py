# Generated by Django 5.1.1 on 2024-09-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_categories_seo_description_categories_seo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=155, null=True, unique=True),
        ),
    ]