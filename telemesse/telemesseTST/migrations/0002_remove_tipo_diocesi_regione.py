# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-18 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telemesseTST', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_diocesi',
            name='regione',
        ),
    ]
