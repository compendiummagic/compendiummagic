# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import django.utils.timezone
from django.conf import settings
import compendium.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compendium', '0003_auto_20170331_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewTrick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('designer', models.CharField(max_length=200)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('quantity', models.IntegerField(default=0)),
                ('cover_image', models.ImageField(default=b'apparel/image_not_available.jpg', upload_to=compendium.models.apparel_cover_upload_path)),
                ('difficulty', models.ForeignKey(to='compendium.Difficulty')),
            ],
        ),
        migrations.CreateModel(
            name='TrickOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(to='compendium.Cart')),
                ('item', models.ForeignKey(to='compendium.Trick')),
            ],
        ),
        migrations.CreateModel(
            name='TrickType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='trick',
            name='type',
            field=models.ForeignKey(to='compendium.TrickType'),
        ),
        migrations.AddField(
            model_name='reviewtrick',
            name='apparel',
            field=models.ForeignKey(to='compendium.Trick'),
        ),
        migrations.AddField(
            model_name='reviewtrick',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
