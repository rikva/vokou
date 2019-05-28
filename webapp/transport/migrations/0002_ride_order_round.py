# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0075_auto_20170819_1316'),
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='order_round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ride', to='ordering.OrderRound'),
        ),
    ]