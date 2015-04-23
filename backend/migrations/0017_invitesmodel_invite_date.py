# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20150310_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitesmodel',
            name='invite_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
