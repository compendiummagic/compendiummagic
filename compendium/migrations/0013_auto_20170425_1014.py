# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0012_auto_20170421_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='firstname',
            field=models.CharField(default='Tom', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='lastname',
            field=models.CharField(default='Dykes', max_length=50),
            preserve_default=False,
        ),
    ]
