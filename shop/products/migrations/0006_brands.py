# Generated by Django 5.1.1 on 2024-09-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_sub_category_categories_upper_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('description', models.TextField(blank=True, null=True)),
                ('seo_title', models.CharField(blank=True, max_length=155, null=True)),
                ('slug', models.SlugField(blank=True, max_length=155, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='brand_pictures')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
    ]
