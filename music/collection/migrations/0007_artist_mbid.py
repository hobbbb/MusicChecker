# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_album_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='mbid',
            field=models.CharField(default=b'', unique=True, max_length=100, verbose_name='mbid'),
        ),
    ]
