# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peepcompare', '0005_auto_20160523_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='facemash',
            name='sender',
            field=models.ForeignKey(related_name='Superuser', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
