# Generated by Django 5.1.1 on 2024-09-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_categories_options_categories_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='seo_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categories',
            name='seo_title',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
