# Generated by Django 5.1.1 on 2024-11-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_tags_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='homepage',
            field=models.BooleanField(default=False),
        ),
    ]