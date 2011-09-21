# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.gammu.models import *

# VCF export: http://vobject.skyhouseconsulting.com/usage.html

DB = 'django-gammu'

def index( request ):
	return HttpResponseRedirect("simplelist")

def simplelist( request ):
	params = {}
	params["Events"] = Events.objects.using(DB).all()
	return render_to_response("simplelist.html", params)

def listing( request ):
	params = {}
	# get current date, show yesterday, today and the next 7 days
	# retrieve matching events from database
	#Events.objects.using( CalendarDB ).all()
	# return array of days, containing the matched events
	params["days"] = [ {'date':'2011-07-22', 'events':[{'id':'1', 'start':'22:00', 'end':'23:00', 'summary':'django-calendar programmieren', 'selected':'checked'}]} ]
	return render_to_response("listing.html", params)

def week( request ):
	params = {}
	params["days"] = ["x" for i in range(0,7)]
	return render_to_response("week.html", params)

def save( request ):
	ID = request.GET.get("id")
	start = request.GET.get("start")
	end = request.GET.get("end")
	summary = request.GET.get("summary")
	if ID == "new":
		e = Events.objects.using(DB).create( start=start, end=end, summary=summary )
	else:
		e = Events.objects.using(DB).get( id=ID )
		e.start = start
		e.end = end
		e.summary = summary
		e.save()
	return HttpResponseRedirect(".")

def delete( request ):
	ID = request.GET.get("id")
	e = Events.objects.using(DB).get( id=ID )
	e.delete()
	return HttpResponseRedirect(".")

