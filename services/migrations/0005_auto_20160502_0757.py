# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-02 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20160502_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=1500),
        ),
    ]
