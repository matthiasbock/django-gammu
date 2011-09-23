# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.gammu.models import *

from datetime import date

# VCF export: http://vobject.skyhouseconsulting.com/usage.html

DB = 'django-gammu'

def index( request ):
	return HttpResponseRedirect("simplelist")

def simplelist( request ):
	params = {}
	params["Events"] = Events.objects.using(DB).all()
	return render_to_response("simplelist.html", params)

def day( request ):
	if not request.GET.has_key("date"):
		return HttpResponseRedirect("day?date="+date.today().strftime("%Y-%m-%d"))
	params = {}
	params["date"] = request.GET.get("date")
	return render_to_response("day.html", params)

def threedays( request ):
	params = {}
	return render_to_response("day.html", params)

def week( request ):
	params = {}
	params["days"] = ["x" for i in range(0,7)]
	return render_to_response("week.html", params)

def month( request ):
	params = {}
	return render_to_response("month.html", params)

def year( request ):
	params = {}
	return render_to_response("year.html", params)


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

