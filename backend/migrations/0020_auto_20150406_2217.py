# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_teachermodel_handout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachermodel',
            name='handout',
        ),
        migrations.AddField(
            model_name='handoutmodel',
            name='teacher_relation',
            field=models.ForeignKey(to='backend.TeacherModel', null=True),
            preserve_default=True,
        ),
    ]
