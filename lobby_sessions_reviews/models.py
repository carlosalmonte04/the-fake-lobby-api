# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from lobby_sessions.models import Session


# Create your models here.
class Review(models.Model):
	score     = models.IntegerField()
	session   = models.ForeignKey(Session)
	time      = models.CharField(max_length=20)