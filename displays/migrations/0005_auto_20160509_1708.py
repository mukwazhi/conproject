# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0004_delete_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='displayimage',
            old_name='display',
            new_name='about_display',
        ),
        migrations.RenameField(
            model_name='displayimage',
            old_name='active',
            new_name='active_slides',
        ),
        migrations.RenameField(
            model_name='displayimage',
            old_name='featured',
            new_name='home_background_display',
        ),
    ]
