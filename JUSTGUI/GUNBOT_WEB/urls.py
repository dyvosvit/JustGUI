"""GUNBOT_WEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
admin.site.site_header = 'Just GUI'

from web.views import index, gui, logs, settings, profit, login_history, trades, start_gb
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', index, name='home'),
    url(r'^accounts/panel/$', gui, name='gui'), 
    url(r'^accounts/logs/$', logs, name='logs'),
    url(r'^accounts/settings/$', settings, name='settings'),
    url(r'^accounts/profit/$', profit, name='profit'),
    url(r'^accounts/history/$', login_history, name='login_history'),
    url(r'^accounts/trades/$', trades, name='trades'),
    url(r'^accounts/start/$', start_gb, name='start_gb'),
    url(r'^accounts/', include('registration.backends.default.urls')),






]
