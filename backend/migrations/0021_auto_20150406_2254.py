# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_auto_20150406_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handoutmodel',
            name='teacher_relation',
        ),
        migrations.DeleteModel(
            name='TeacherModel',
        ),
        migrations.AddField(
            model_name='handoutmodel',
            name='user_relation',
            field=models.ForeignKey(to='backend.UsersModel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usersmodel',
            name='is_teacher',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
