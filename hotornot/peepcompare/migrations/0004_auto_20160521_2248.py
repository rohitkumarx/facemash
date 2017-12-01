# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peepcompare', '0003_auto_20160519_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facemash',
            name='rd',
        ),
        migrations.RemoveField(
            model_name='facemash',
            name='sigma',
        ),
        migrations.AlterField(
            model_name='facemash',
            name='ratings',
            field=models.FloatField(default=100),
        ),
    ]
