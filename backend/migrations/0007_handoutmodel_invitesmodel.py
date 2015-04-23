# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_user_test1'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandoutModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handout_id', models.IntegerField(unique=True, null=True)),
                ('teacher', models.CharField(max_length=128, null=True)),
                ('period', models.IntegerField(null=True)),
                ('file_name', models.CharField(max_length=128, null=True)),
                ('date', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvitesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=128, null=True)),
                ('invite_id', models.IntegerField(unique=True, null=True)),
                ('handout', models.ForeignKey(to='backend.HandoutModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
