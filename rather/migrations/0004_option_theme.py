# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rather', '0003_remove_option_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='theme',
            field=models.CharField(default='hello', max_length=200),
            preserve_default=False,
        ),
    ]