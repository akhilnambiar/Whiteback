# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_user_test1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='test1',
        ),
    ]
