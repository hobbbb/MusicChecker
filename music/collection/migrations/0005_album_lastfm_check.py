# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_artist_lastfm_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='lastfm_check',
            field=models.BooleanField(default=0, verbose_name='\u0421\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u0435 \u0441 Last.fm'),
        ),
    ]
