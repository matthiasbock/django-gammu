# -*- coding: iso-8859-15 -*-

#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

#from Django.globals import *
#from Django.contacts.models import *

def index(request):
	return render_to_response("sync.html")

