# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0010_shippinginfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippinginfo',
            name='county',
            field=models.CharField(default='West Yorkshire', max_length=200),
            preserve_default=False,
        ),
    ]
