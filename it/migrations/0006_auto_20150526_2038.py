# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0005_auto_20150526_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='id',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='id',
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
