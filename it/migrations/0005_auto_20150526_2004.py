# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0004_language_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itmanual',
            name='language',
            field=models.ForeignKey(to='it.Language'),
        ),
        migrations.AlterField(
            model_name='itmanual',
            name='topic',
            field=models.ForeignKey(to='it.Topic'),
        ),
    ]
