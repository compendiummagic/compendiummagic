# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0006_auto_20170403_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficulty',
            name='title',
            field=models.CharField(default='x Stars', max_length=200),
            preserve_default=False,
        ),
    ]
