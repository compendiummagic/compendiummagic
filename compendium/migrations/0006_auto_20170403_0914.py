# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import compendium.models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0005_auto_20170331_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty',
            name='rating',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trick',
            name='cover_image',
            field=models.ImageField(default=b'trick/image_not_available.jpg', upload_to=compendium.models.trick_cover_upload_path),
        ),
    ]
