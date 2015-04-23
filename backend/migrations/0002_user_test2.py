# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test2',
            field=models.CharField(max_length=128, unique=True, null=True),
            preserve_default=True,
        ),
    ]
