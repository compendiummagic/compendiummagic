# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import compendium.models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0007_difficulty_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('restaurant', models.BooleanField(default=False)),
                ('stage', models.BooleanField(default=False)),
                ('close_up', models.BooleanField(default=False)),
                ('bio', models.TextField()),
                ('speciality', models.CharField(default=b'All-Rounder', max_length=200)),
                ('image', models.ImageField(default=b'image_not_available.jpg', upload_to=compendium.models.act_cover_upload_path)),
                ('website', models.CharField(default=b'http://localhost:8000/compendiummagic/', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='difficulty',
            name='title',
        ),
        migrations.AlterField(
            model_name='apparel',
            name='cover_image',
            field=models.ImageField(default=b'image_not_available.jpg', upload_to=compendium.models.apparel_cover_upload_path),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default=b'image_not_available.jpg', upload_to=compendium.models.book_cover_upload_path),
        ),
        migrations.AlterField(
            model_name='misc',
            name='cover_image',
            field=models.ImageField(default=b'image_not_available.jpg', upload_to=compendium.models.misc_cover_upload_path),
        ),
        migrations.AlterField(
            model_name='trick',
            name='cover_image',
            field=models.ImageField(default=b'image_not_available.jpg', upload_to=compendium.models.trick_cover_upload_path),
        ),
        migrations.AddField(
            model_name='act',
            name='style',
            field=models.ForeignKey(to='compendium.ActStyle'),
        ),
    ]
