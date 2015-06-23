# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0002_itmanual_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itmanual',
            name='title',
        ),
    ]
