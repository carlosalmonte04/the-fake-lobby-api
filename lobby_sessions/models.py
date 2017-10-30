# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Session(models.Model):
	insider   = models.ForeignKey(User, related_name='insider')
	jobSeeker = models.ForeignKey(User, related_name='jobSeeker')
	date      = models.DateField()
	title     = models.TextField()
	comments  = models.TextField()
	time      = models.CharField(max_length=20)