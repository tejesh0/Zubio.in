# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_auto_20150401_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fitnesslisting',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='fitnesslisting',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='fitnesslisting',
            old_name='docfile',
            new_name='Gallery',
        ),
        migrations.RemoveField(
            model_name='fitnesslisting',
            name='fit_name',
        ),
        migrations.RemoveField(
            model_name='fitnesslisting',
            name='isMembership',
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='AC',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Certified_Trainer',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Choose_Fitness_Center_category',
            field=models.CharField(default=b'Gym', max_length=20, choices=[(b'Gym', b'Gym'), (b'Spa', b'Spa'), (b'Yoga Center', b'Yoga Center'), (b'Salon', b'Salon')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Email',
            field=models.EmailField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Half_yearly',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Locker',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Membership',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Monthly',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Name_Of_The_Fitness_Center',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Owners_Name',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Parking',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Personal_Trainer',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Quaterly',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='WiFi',
            field=models.CharField(default=b'No', max_length=4, choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='Yearly',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fitnesslisting',
            name='phone_number',
            field=models.CharField(default=b'', max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'")]),
            preserve_default=True,
        ),
    ]
