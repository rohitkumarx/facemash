# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peepcompare', '0006_facemash_sender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facemash',
            old_name='sender',
            new_name='user',
        ),
    ]
