# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peepcompare', '0004_auto_20160521_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facemash',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
