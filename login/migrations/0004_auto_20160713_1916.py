# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_freelancer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freelancer',
            old_name='firstname',
            new_name='Password',
        ),
        migrations.RenameField(
            model_name='freelancer',
            old_name='interest',
            new_name='field_of_interest',
        ),
        migrations.RenameField(
            model_name='freelancer',
            old_name='lastname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='freelancer',
            old_name='skils',
            new_name='skills',
        ),
    ]
