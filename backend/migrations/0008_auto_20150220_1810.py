# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_handoutmodel_invitesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(unique=True, max_length=128)),
                ('first_name', models.CharField(max_length=128, null=True)),
                ('last_name', models.CharField(max_length=128, null=True)),
                ('teacher', models.CharField(max_length=128, null=True)),
                ('school', models.CharField(max_length=128, null=True)),
                ('period', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=128, unique=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
