# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='goods')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(max_length=20, default='500g')),
                ('gclick', models.IntegerField()),
                ('gjianjie', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField()),
                ('gcontent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('css', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='tt_goods.TypeInfo'),
        ),
    ]
