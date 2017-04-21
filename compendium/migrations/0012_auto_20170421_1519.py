# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0011_shippinginfo_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='website',
            field=models.CharField(default=b'http://www.compendiummagic.co.uk/hire_us/0/', max_length=200),
        ),
    ]
