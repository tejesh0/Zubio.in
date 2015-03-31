# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20150313_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.CharField(default=b'Description', max_length=500),
            preserve_default=True,
        ),
    ]
