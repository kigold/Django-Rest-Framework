# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0011_auto_20170607_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
