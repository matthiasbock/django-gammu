# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.databases import *
from Django.gammu.models import *

def index( request ):
	return HttpResponseRedirect("simplelist")

def simplelist( request ):
	params = {}
	params["Events"] = Events.objects.using('django-gammu').all()
	return render_to_response("simplelist.html", params)

def listing( request ):
	params = {}
	# get current date, show yesterday, today and the next 7 days
	# retrieve matching events from database
	#Events.objects.using( CalendarDB ).all()
	# return array of days, containing the matched events
	params["days"] = [ {'date':'2011-07-22', 'events':[{'id':'1', 'start':'22:00', 'end':'23:00', 'summary':'django-calendar programmieren', 'selected':'checked'}]} ]
	return render_to_response("listing.html", params)

#http://vobject.skyhouseconsulting.com/usage.html

def save( request ):
	return HttpResponseRedirect("listing")

