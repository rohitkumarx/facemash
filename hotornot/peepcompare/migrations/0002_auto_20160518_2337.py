# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peepcompare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facemash',
            name='photo',
            field=models.ImageField(upload_to=b'facemash_photos/%Y/%m/%d'),
        ),
    ]
