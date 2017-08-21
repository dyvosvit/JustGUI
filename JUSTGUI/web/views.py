from django.shortcuts import render

# Create your views here.

import urllib2
import json
from datetime import datetime, timedelta
from decimal import *
import datetime as DT
import datetime
from .forms import SettingsForm
import random, string

from user.models import gain, ip, API


def index(request):

	return render(request, 'gui/justgui.html', {})

def gui(request):


	username = None

	if request.user.is_authenticated():
		username = request.user.username
		get_user_ip(request)

	ip_api = API.objects.all()
	for ip in ip_api:
		ip = ip.ip

		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()

	try:

		balance = api[13:50]
		print balance
		user_gain = api[73:80]
		print user_gain

		time = datetime.datetime.now()
		datos_usuario = gain.objects.get_or_create(user = username, balance = Decimal(balance[:7]), profit = Decimal(user_gain[:7]), timestamp =  time.strftime("%Y-%m-%d"))
		user_static = gain.objects.filter(user= username).order_by('timestamp')[:1]
		for instance in user_static:
			profit_1 = str(instance.profit)
			timestamp_1 = instance.timestamp

		user_static = gain.objects.filter(user = username).order_by('timestamp')[:2]
		for instance in user_static:
			profit_2 = str(instance.profit)
			timestamp_2 = instance.timestamp

		user_static = gain.objects.filter(user = username).order_by('timestamp')[:]
		for instance in user_static:
			profit_3 = str(instance.profit)		
			timestamp_3 = instance.timestamp

		return render(request, 'gui/index.html', {'balances':balance[:7], 'gain':user_gain[:7], 'username':username, 'profit_1':str(profit_1), 'timestamp_1':timestamp_1,'profit_2':profit_2, 'timestamp_2':timestamp_2, 'profit_3':profit_3, 'timestamp_3':timestamp_3})

	except Exception as e:
		balance = 'No data'
		user_gain = 'No data'



	return render(request, 'gui/index.html', {'balances':balance[:7], 'gain':user_gain[:7], 'username':username,})

def logs(request):

	username = None

	if request.user.is_authenticated():
		username = request.user.username

	ip_api = API.objects.all()
	for ip in ip_api:
		ip = ip.ip


	try:
		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()
		balance = api[13:69]
		gain = api[73:80]

		logs = urllib2.urlopen('http://%s:4523/logs' % (ip)).read()

		
	except Exception as e:
		balance = 'No data'
		gain = 'No data'
		logs = 'No data'
	return render(request, 'gui/logs.html', {'logs':logs, 'balances':balance[:7], 'gain':gain[:7], 'username':username})

def settings(request):


	username = None

	if request.user.is_authenticated():
		username = request.user.username
	
	ip_api = API.objects.all()
	for ip in ip_api:
		ip = ip.ip
	try:
		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()
		balance = api[13:69]
		gain = api[73:80]

		logs = urllib2.urlopen('http://%s:4523/logs' % (ip)).read()

	except Exception as e:
		balance = 'No data'
		gain = 'No data'

	settings_form = SettingsForm(request.POST, request.FILES or None)

	if settings_form.is_valid():
		config = settings_form.cleaned_data['config']
		random_str = ''.join(random.choice(string.lowercase) for i in range(10))

		file = open('user_config/'+str(random_str), 'wb')
		file.write(str(config))
		file.close()
		try:
			os.system('nc -w 3 %s 1234 < user_config/'+str(random_str) % (ip))
		except Exception as e:
			print ('No se puede subir')

	return render(request, 'gui/settings.html', {'balances':balance[:7], 'gain':gain[:7], 'username':username,'settings_form':settings_form,})

def profit(request):

	username = None

	if request.user.is_authenticated():
		username = request.user.username
	
	ip_api = API.objects.all()
	for ip in ip_api:
		ip = ip.ip
	
	try:
		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()
		balance = api[13:69]
		gain_user = api[73:80]

	except Exception as e:
		balance = 'No data'
		gain_user = 'No data'

	today = DT.date.today()
	week_ago = today - DT.timedelta(days=7)

	gain_ago = gain.objects.filter(timestamp = week_ago)

	for instance in gain_ago:
		gain_ago = str(instance.profit)

	if len(gain_ago) == 0:
		gain_ago = 0

	gain_now = gain.objects.filter(timestamp = today)
	for instance in gain_now:
		gain_now = instance.profit

	return render(request, 'gui/profit.html', {'balances':balance[:7], 'gain':gain_user[:7], 'gain_now':gain_now, 'gain_ago':gain_ago, 'username':username})


def login_history(request):

	username = None

	if request.user.is_authenticated():
		username = request.user.username
	
	ip_api = API.objects.all()
	for ip in ip_api:
		ip = ip.ip
	try:
		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()
		balance = api[13:69]
		gain_user = api[73:80]

	except Exception as e:
		balance = 'No data'
		gain_user = 'No data'

	ip_user = ip.objects.filter(user = "%s" % (username))

	return render(request, 'gui/login-history.html', {'balances':balance[:7], 'gain':gain_user[:7], 'ip_user':ip_user, 'username':username})

def trades(request):

	username = None

	if request.user.is_authenticated():
		username = request.user.username

	ip_api = API.objects.all()
	for ip in ip_api:
		ip = ip.ip

	try:
		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()
		balance = api[13:69]
		gain_user = api[73:80]

		trades = urllib2.urlopen('http://%s:4523/trades' % (ip)).read()

		if len(trades) == 0:
			trades = 'No trades has been performed'
	except Exception as e:
		balance = 'No data'
		gain_user = 'No data'
		logs = 'No data'
		trades = 'No data'

	return render(request, 'gui/trades.html', {'balances':balance[:7], 'gain':gain_user[:7], 'trades':trades, 'username':username})


def start_gb(request):

	username = None

	if request.user.is_authenticated():
		username = request.user.username

	try:
		api = urllib2.urlopen('http://%s:4523/all' % (ip)).read()
		balance = api[13:69]
		gain_user = api[73:80]

		start = urllib2.urlopen('http://%s:4523/start' % ip).read()
		message = "GB has been started successfully. Good luck with the trading."
	
	except Exception as e:
		balance = 'No data'
		gain_user = 'No data'
		start = "GB could not be started, check that the Uservzk80 service is running on your server."
		message = start
	return render(request, 'gui/start.html', {'message':message})

def get_user_ip(request):

	now = datetime.datetime.now()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

	ip_user = request.META.get('REMOTE_ADDR')

	if request.user.is_authenticated():
		username = request.user.username

	ip_save = ip.objects.get_or_create(user = username, ip = ip_user, timestamp = now.strftime("%Y-%m-%d"))
