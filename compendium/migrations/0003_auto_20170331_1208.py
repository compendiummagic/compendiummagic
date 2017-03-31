# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compendium', '0002_reviewapparel_reviewbook_reviewmisc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApparelOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('order_date', models.DateField(null=True)),
                ('payment_type', models.CharField(max_length=100, null=True)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MiscOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(to='compendium.Cart')),
                ('item', models.ForeignKey(to='compendium.Misc')),
            ],
        ),
        migrations.AddField(
            model_name='bookorder',
            name='cart',
            field=models.ForeignKey(to='compendium.Cart'),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='item',
            field=models.ForeignKey(to='compendium.Book'),
        ),
        migrations.AddField(
            model_name='apparelorder',
            name='cart',
            field=models.ForeignKey(to='compendium.Cart'),
        ),
        migrations.AddField(
            model_name='apparelorder',
            name='item',
            field=models.ForeignKey(to='compendium.Apparel'),
        ),
    ]
