# Generated by Django 5.1.6 on 2025-03-18 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
        ('user', '0002_remove_customer_book_buy'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduaction_book',
            name='book_buy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_book', to='user.customer'),
        ),
    ]
