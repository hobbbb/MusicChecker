# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_artist_mbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='mbid',
            field=models.CharField(max_length=100, verbose_name='mbid'),
        ),
    ]
