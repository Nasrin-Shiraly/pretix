# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 11:29
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pretixbase', '0094_auto_20180604_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='oauth_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='pretixapi.OAuthApplication'),
        ),
    ]
