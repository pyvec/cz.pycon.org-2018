# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_auto_20180528_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['position']},
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='date_created',
        ),
        migrations.AddField(
            model_name='announcement',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
