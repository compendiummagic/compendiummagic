# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0004_auto_20170331_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewtrick',
            old_name='apparel',
            new_name='trick',
        ),
    ]
