# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-22 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamlogic', '0012_auto_20170621_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchinleague',
            name='tour1',
        ),
    ]
