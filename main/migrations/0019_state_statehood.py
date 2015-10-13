# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_state_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='statehood',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
