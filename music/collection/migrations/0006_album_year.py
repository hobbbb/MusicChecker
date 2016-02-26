# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_album_lastfm_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.CharField(default=b'', max_length=4, verbose_name='\u0413\u043e\u0434'),
        ),
    ]
