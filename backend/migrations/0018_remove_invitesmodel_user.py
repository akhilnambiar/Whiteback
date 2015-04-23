# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_invitesmodel_invite_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitesmodel',
            name='user',
        ),
    ]
