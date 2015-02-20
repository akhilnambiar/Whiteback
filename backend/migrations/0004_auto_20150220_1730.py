# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_user_test2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='test',
        ),
        migrations.RemoveField(
            model_name='user',
            name='test1',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=128, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='period',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
