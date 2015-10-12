# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150930_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state_abbrev',
        ),
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='lon',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
