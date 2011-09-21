# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
from Django.contacts.models import *

# http://www.ietf.org/rfc/rfc2426.txt

def index( request ):
	return HttpResponseRedirect("contacts")

def Table( request ):
	params = {}
	alphabet = map(chr, range(65, 91))
	maxcol = 6
	col = maxcol
	params["rows"] = []						# generate table from alphabet
	location = {}
	for char in alphabet:
		if col >= maxcol:
			params["rows"].append( [] )			# new, empty row
			col = 0
		column = {'char':char, 'contacts':[]}			# new column
		lastrow = len(params["rows"])-1				# find last row
		params["rows"][lastrow].append( column )		# lastrow.append( column )
		location[char] = {'row':lastrow, 'col':col}
		col = len(params["rows"][lastrow])			# count columns in lastrow
	for contact in Contacts.objects.using(ContactsDB).filter(owner=1):
		if contact.familyname != "":
			char = contact.familyname[0].upper()
		else:
			char = contact.firstname[0].upper()
		params["rows"][ location[char]['row'] ][ location[char]['col'] ]['contacts'].append( contact )
	return render_to_response("contacts_table.html", params)

def EditContact( request ):
	if request.method == "GET":
		params = {}
		ID = request.GET.get("contact")
		contact = Contacts.objects.using( ContactsDB ).get( id=ID )
		params["id"]		= ID
		params["firstname"]	= contact.firstname
		params["familyname"]	= contact.familyname
		params["atoms"]		= Atoms.objects.using(ContactsDB).filter( contact=ID )
	#	params["address"]	= Address.objects.using( ContactsDB ).filter( contact=ID )
		return render_to_response("contacts_edit.html", params)
	else:
		# ... Save button
		pass

def RemoveContact( request ):
	contact = Contacts.objects.using(ContactsDB).get( id=request.GET.get("contact") )
	contact.owner = 0									# don't actually delete contact, only set owner=0
	contact.save()
	return HttpResponse("<script>parent.location.href='table';</script>", "text/html")	# reload parent frame

def AddAtom( request ):
	params = {}
	property = request.POST.get("property")
	contact = request.POST.get("contact")
	type = request.POST.get("type")
	value = request.POST.get("value")
	Atoms.objects.using( ContactsDB ).create( property=property, contact=contact, type=type, value=value )
	return HttpResponseRedirect("edit?contact="+contact)

def RemoveAtom( request ):
	atom = request.GET.get("atom")
	atom = Atoms.objects.using(ContactsDB).get( id=atom )
	atom.contact = 0
	atom.save()
	contact = request.GET.get("contact")
	return HttpResponseRedirect("edit?contact="+contact)

