# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0034_auto_20160728_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='loneplayerpairing',
            name='pairing_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teampairing',
            name='pairing_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]