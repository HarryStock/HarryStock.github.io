# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0006_auto_20150526_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='itmanual',
            name='title',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 5, 26, 20, 52, 56, 815345, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
