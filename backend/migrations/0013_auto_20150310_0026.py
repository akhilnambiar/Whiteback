# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20150309_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handoutmodel',
            name='handout_id',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
