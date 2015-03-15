# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='address',
            field=models.CharField(default=b'please fill', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default=b'please fill', max_length=50),
            preserve_default=True,
        ),
    ]
