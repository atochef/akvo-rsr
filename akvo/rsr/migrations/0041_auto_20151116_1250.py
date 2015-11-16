# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsr', '0040_auto_20151111_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sector',
            options={'ordering': ['sector_code'], 'verbose_name': 'sector', 'verbose_name_plural': 'sectors'},
        ),
        migrations.AddField(
            model_name='project',
            name='is_private',
            field=models.BooleanField(default=False, help_text='Determines whether this project is a private project.', verbose_name='is private project'),
            preserve_default=True,
        ),
    ]
