# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20160226_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='mbid',
            field=models.CharField(default=b'', max_length=100, verbose_name='mbid'),
        ),
    ]
