# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20150310_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handoutmodel',
            old_name='google_identifier',
            new_name='google_id',
        ),
    ]
