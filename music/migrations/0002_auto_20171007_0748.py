# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='artist',
            new_name='artist_name',
        ),
    ]
