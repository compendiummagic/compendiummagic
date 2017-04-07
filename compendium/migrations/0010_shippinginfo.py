# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compendium', '0009_item_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_name', models.CharField(max_length=200)),
                ('house_number', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
