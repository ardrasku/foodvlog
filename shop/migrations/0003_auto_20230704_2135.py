# Generated by Django 2.2 on 2023-07-04 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
