# -*- coding: utf-8 -*-
from django.db import models

class Artist(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=100, unique=True)
    lastfm_check = models.BooleanField(verbose_name=u'Совпадение с Last.fm', default=0)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey('Artist', verbose_name=u'Артист')
    name   = models.CharField(verbose_name=u'Название', max_length=150)
    year   = models.CharField(verbose_name=u'Год', max_length=4, default='')
    lastfm_check = models.BooleanField(verbose_name=u'Совпадение с Last.fm', default=0)

    def __unicode__(self):
        return self.name
