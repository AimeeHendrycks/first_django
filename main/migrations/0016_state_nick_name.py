# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151012_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='nick_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
