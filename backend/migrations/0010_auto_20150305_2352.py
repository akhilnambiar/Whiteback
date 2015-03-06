# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20150224_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=128, null=True)),
                ('first_name', models.CharField(max_length=128, null=True)),
                ('last_name', models.CharField(max_length=128, null=True)),
                ('school', models.CharField(max_length=128, null=True)),
                ('period', models.CharField(max_length=128, null=True)),
                ('email', models.CharField(max_length=128, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='handoutmodel',
            old_name='date',
            new_name='due_date',
        ),
        migrations.AddField(
            model_name='handoutmodel',
            name='google_identifier',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='handoutmodel',
            name='invite_id',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='handoutmodel',
            name='push_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
