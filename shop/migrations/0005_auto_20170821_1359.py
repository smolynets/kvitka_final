# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-21 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.CharField(max_length=256),
        ),
    ]
