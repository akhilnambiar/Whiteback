# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20150406_2254'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GTLFiles',
        ),
        migrations.AddField(
            model_name='handoutmodel',
            name='thumbnailLink',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
