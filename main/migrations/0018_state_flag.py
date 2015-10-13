# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_state_bird'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='flag',
            field=models.ImageField(null=True, upload_to=b'flag', blank=True),
        ),
    ]
