# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20150220_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitesmodel',
            name='invitee',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitesmodel',
            name='inviter',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
