# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceMash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to=b'facemash_photos')),
                ('ratings', models.FloatField(default=1500)),
                ('rd', models.FloatField(default=350)),
                ('sigma', models.FloatField(default=0.06)),
            ],
            options={
                'verbose_name_plural': 'Facemash',
            },
        ),
    ]
