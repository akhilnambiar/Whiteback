# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20150305_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersmodel',
            name='period',
            field=backend.models.ListField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usersmodel',
            name='teacher',
            field=backend.models.ListField(null=True),
            preserve_default=True,
        ),
    ]
