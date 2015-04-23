# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20150306_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='GTLFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('google_id', models.CharField(max_length=128, null=True)),
                ('title', models.CharField(max_length=128, null=True)),
                ('thumbnailLink', models.CharField(max_length=128, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='period',
            field=backend.models.ListField(null=True),
            preserve_default=True,
        ),
    ]
