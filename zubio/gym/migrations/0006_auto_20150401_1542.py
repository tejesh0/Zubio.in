# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_auto_20150401_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesslisting',
            name='address',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fitnesslisting',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
