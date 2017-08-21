# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import gain, ip, API
admin.site_header = 'JustGUI'

class adminGain(admin.ModelAdmin):

	list_display = ['__unicode__', 'balance', 'profit', 'timestamp']

	class Meta:
		model = gain

admin.site.register(gain, adminGain)

class adminIp(admin.ModelAdmin):

	list_display = ['__unicode__', 'ip', 'timestamp']

	class Meta:
		model = ip
admin.site.register(ip, adminIp)

class adminAPI(admin.ModelAdmin):

	list_display = ['__unicode__']

	class Meta:
		model = API
admin.site.register(API, adminAPI)