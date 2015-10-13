# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_state_nick_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='bird',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
