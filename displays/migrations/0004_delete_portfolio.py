# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-30 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0003_auto_20160423_1753'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]