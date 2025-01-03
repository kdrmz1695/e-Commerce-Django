# Generated by Django 5.1.1 on 2024-09-08 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='categories',
            name='sub_category',
            field=models.ForeignKey(blank=True, help_text='If this category related with another category please fill in here.', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categories'),
        ),
    ]
