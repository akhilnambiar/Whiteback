# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20150310_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitesmodel',
            name='invite_id',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
