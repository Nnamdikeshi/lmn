# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-04-13 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0005_note_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='photo',
        ),
    ]
