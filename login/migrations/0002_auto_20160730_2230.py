# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='name',
            field=models.CharField(max_length=20, unique=False, verbose_name=b'name'),
        ),
    ]
