# Generated by Django 5.1.6 on 2025-03-18 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='book_buy',
        ),
    ]
