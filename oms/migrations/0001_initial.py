# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Progame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AppID', models.IntegerField()),
                ('AppName', models.CharField(max_length=50)),
                ('ProName', models.CharField(max_length=40)),
                ('Domain', models.CharField(max_length=100)),
                ('Apptype', models.CharField(max_length=40)),
            ],
        ),
    ]
