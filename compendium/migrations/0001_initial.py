# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import compendium.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apparel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('designer', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('quantity', models.IntegerField(default=0)),
                ('cover_image', models.ImageField(default=b'apparel/image_not_available.jpg', upload_to=compendium.models.apparel_cover_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='ApparelSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ApparelType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('quantity', models.IntegerField(default=0)),
                ('cover_image', models.ImageField(default=b'books/image_not_available.jpg', upload_to=compendium.models.book_cover_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('designer', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('quantity', models.IntegerField(default=0)),
                ('cover_image', models.ImageField(default=b'misc/image_not_available.jpg', upload_to=compendium.models.misc_cover_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='MiscType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='misc',
            name='type',
            field=models.ForeignKey(to='compendium.MiscType'),
        ),
        migrations.AddField(
            model_name='apparel',
            name='size',
            field=models.ForeignKey(to='compendium.ApparelSize'),
        ),
        migrations.AddField(
            model_name='apparel',
            name='type',
            field=models.ForeignKey(to='compendium.ApparelType'),
        ),
    ]
