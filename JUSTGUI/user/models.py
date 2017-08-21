# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
ADMIN_TITLE = "JustGUI Admin"

ADMIN_BRAND_TITLE = "JustGUI Admin"

class gain(models.Model):

	user = models.CharField(max_length=25)
	balance = models.DecimalField(max_digits=19, decimal_places=10)
	profit = models.DecimalField(max_digits=19, decimal_places=10)
	timestamp = models.DateTimeField(auto_now_add = False)
	def __unicode__(self):

		return unicode(self.user)

class API(models.Model):

	ip = models.GenericIPAddressField()

	def __unicode__(self):
		return unicode(self.ip)

class ip(models.Model):

	user = models.CharField(max_length=25)
	ip = models.GenericIPAddressField()
	timestamp = models.DateTimeField(auto_now_add = False)

	def __unicode__(self):
		return self.user