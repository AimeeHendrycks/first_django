# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20151006_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='pop',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
