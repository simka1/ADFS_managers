# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-17 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamlogic', '0005_auto_20170317_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time1', models.TimeField()),
                ('time2', models.TimeField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamlogic.Match')),
                ('stadion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamlogic.Stadium')),
            ],
        ),
    ]
