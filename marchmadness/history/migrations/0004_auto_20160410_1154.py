# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_chancewin'),
    ]

    operations = [
        migrations.AddField(
            model_name='chancewin',
            name='gameID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pastgame',
            name='gameID',
            field=models.IntegerField(default=0),
        ),
    ]
