# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20150310_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitesmodel',
            name='handout',
        ),
        migrations.AddField(
            model_name='invitesmodel',
            name='handout_id',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitesmodel',
            name='invitee',
            field=backend.models.ListField(null=True),
            preserve_default=True,
        ),
    ]
