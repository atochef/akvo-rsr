# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsr', '0120_auto_20180108_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indicatorperiod',
            options={'ordering': ['period_start', 'period_end'], 'verbose_name': 'indicator period', 'verbose_name_plural': 'indicator periods'},
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='baseline_value',
        ),
        migrations.RenameField(
            model_name='indicator',
            old_name='new_baseline_value',
            new_name='baseline_value'
        ),
        migrations.RemoveField(
            model_name='indicatorperiod',
            name='target_value',
        ),
        migrations.RenameField(
            model_name='indicatorperiod',
            old_name='new_target_value',
            new_name='target_value'
        ),
        migrations.RemoveField(
            model_name='indicatorperioddata',
            name='value',
        ),
        migrations.RenameField(
            model_name='indicatorperioddata',
            old_name='new_value',
            new_name='value'
        ),
    ]
