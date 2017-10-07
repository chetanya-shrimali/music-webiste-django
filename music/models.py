# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Record(models.Model):
    artist_name = models.CharField(max_length=50)
    record_name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    record_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.record_name + ' -> ' + self.artist_name


class Song(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=25)
    song_title = models.CharField(max_length=50)

    def __str__(self):
        return self.song_title
