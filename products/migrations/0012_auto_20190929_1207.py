# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-29 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_titmestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='titmestamp',
            new_name='timestamp',
        ),
    ]
