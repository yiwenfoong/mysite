# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rather', '0002_option_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='theme',
        ),
    ]