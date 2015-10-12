# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, to='main.State', null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='state_abbrev',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
    ]
