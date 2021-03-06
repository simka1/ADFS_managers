# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-25 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlogic', '0020_auto_20170722_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, default=b'./404/profile.jpg', null=True, upload_to=b'./players'),
        ),
        migrations.AlterField(
            model_name='stadium',
            name='image',
            field=models.ImageField(blank=True, default=b'./404/stadion.jpg', null=True, upload_to=b'./stadions'),
        ),
    ]
