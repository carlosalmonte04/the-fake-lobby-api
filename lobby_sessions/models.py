# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Session(models.Model):
	insider   = models.ForeignKey(User, related_name='insider', on_delete=models.CASCADE)
	jobSeeker = models.ForeignKey(User, related_name='jobSeeker', on_delete=models.CASCADE)
	date      = models.DateField()
	title     = models.TextField()
	comments  = models.TextField(blank=True, default='')
	time      = models.CharField(max_length=20)
	