# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_document_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fit_name', models.CharField(max_length=100)),
                ('address', models.CharField(default=b'please fill', max_length=500)),
                ('description', models.TextField(default=b'Description')),
                ('isMembership', models.CharField(max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
