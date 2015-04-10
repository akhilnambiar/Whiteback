# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_remove_invitesmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='handout',
            field=models.ForeignKey(to='backend.HandoutModel', null=True),
            preserve_default=True,
        ),
    ]
