# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20150401_1531'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FitnessForm',
            new_name='FitnessListing',
        ),
    ]
