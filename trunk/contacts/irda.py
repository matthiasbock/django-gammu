# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
from Django.contacts.models import *
import os
from subprocess import Popen, PIPE
from shlex import split
import gammu

def attach(device):						# attach inactive irda device
	cmd = str("/usr/sbin/irattach "+device+" -s")		# seems to be running as root
	stdout = Popen(split(cmd), stdout=PIPE).communicate()[0]
	open("/tmp/out.txt","w").write(cmd)

def hardware( auto_attach=True ):				# list the available IrDA hardware
	result = []
	syspath = "/sys/class/net"
	if os.path.exists(syspath):
		for filename in os.listdir(syspath):							# check for irda device files in /sys/class/net
			if filename[:4] == "irda":
				dev = {}
				dev["name"] = filename							# device name
				dev["address"] = open(syspath+"/"+filename+"/address").read().strip()	# device address
				if dev["address"][:11] == "00:00:00:00" and auto_attach:		# device is still inactive
					attach(filename)						# activate it !
				result.append(dev)
	return result

def discovered():						# list the IrDA device discovered by the IrDA driver
	result = []
	log = "/proc/net/irda/discovery"
	discovered = open(log).read().split("\n")
	for line in discovered:
		if len(line) > 0 and line[:8] == "nickname":			# device discovered !
			dev = {}
			s = line.split(",")
			dev["name"] = s[0].split(":")[1].strip()		# remote device name
			dev["address"] = s[3].split(":")[1].strip()		# remote device address
			dev["device"] = "/dev/ircomm0"				# remote device's /dev/-port; currently hardcoded, how to automate that?
			result.append(dev)
	return result

def index(request):
	params = {}
	params["hardware"] = hardware()
	params["devices"] = discovered()
	return render_to_response("irda.html", params)

def download(request):
	Device = request.GET.get("dev")						# setup connection
	Connection = "at115200"

	# ... future: do irdaping before invoking gammu !

	phone = gammu.StateMachine()						# init gammu
	phone.SetConfig(0, {"Device":Device, "Connection":Connection})		# config
	phone.Init()								# connect
#	manufacturer = phone.GetManufacturer()					# for debug purposes
#	model = phone.GetModel()[1]

	params = {}
	params["contacts"] = []

	def ResolveRealName(entry):
		try:	# exact name ?
			Contacts.objects.using(ContactsDB).filter( firstname=entry['Firstname'], familyname=entry['Familyname'] )
			return str(entry['Firstname']+" "+entry['Familyname']).strip(" ")
		except:
			# no exact match
			pass
		try:	# try only with first name
			results = Contacts.objects.using(ContactsDB).filter( firstname=entry['Firstname'] )
			if len(results) > 1:
				# too bad, more than one entry with this first name
				raise
			else:	# one match
				entry = results[0]
				return str(entry.firstname+" "+entry.familyname).strip(" ")
		except:
			# not even one or more than one entry with only the first name matching
			pass
		try:	# try if the first part of the name matches a nickname
			results = Nicknames.objects.using(ContactsDB).filter( nick=str(entry['Firstname']+" "+entry['Familyname']).strip(" ").split(" ")[0] )
			if len(results) > 1:
				# that's a problem, nicknames should only occur once!
				raise
			else:	# one match
				return results[0].real.strip(" ")
		except:
			# no nickname
			pass
		# must be a new contact
#		return str(entry['Firstname']+" "+entry['Familyname']).strip(" ")
		return "?"

	def download(type):
		status = phone.GetMemoryStatus( Type=type )			# download all contacts
		remain = status['Used']
		start = True
		while remain > 0:
			if start:
				entry = phone.GetNextMemory(Start = True, Type = type)	# contact by contact ...
				start = False
			else:
				entry = phone.GetNextMemory(Location = entry['Location'], Type = type)
			remain = remain - 1

			new = {'index':len(params["contacts"]), 'ID':entry['Location'], 'Firstname':'', 'Familyname':'', 'Mobile':'', 'Work':'', 'General':''}
			for data in entry['Entries']:				# parse downloaded contact
				if data['Type'] == "Text_FirstName":
					new['Firstname'] = data['Value']
				elif data['Type'] == "Text_LastName" or data['Type'] == 'Text_Name':
					new['Familyname'] = data['Value']
				elif data['Type'] == 'Number_Mobile':
					new['Mobile'] = data['Value']
				elif data['Type'] == 'Number_Work':
					new['Work'] = data['Value']
				elif data['Type'] == 'Number_General':
					new['General'] = data['Value']
			new['Real'] = ResolveRealName(new)
			params["contacts"].append( new )

	download("SM")	# SIM Memory
	download("ME")	# Phone Memory
	phone.Terminate()							# disconnect gammu

	params["number"] = len(params["contacts"])
	return render_to_response("irda_downloaded.html", params)

def save( request ):
	for contact in []:	#request.POST.get("downloaded"):
		if False:	#saveit:
			try:
				r = Contacts.objects.using(ContactsDB).get( firstname=d['Firstname'], familyname=d['Familyname'] )
			except:
				Contacts.objects.using(ContactsDB).create( firstname=d['Firstname'], familyname=d['Familyname'] )
				r = Contacts.objects.using(ContactsDB).get( firstname=d['Firstname'], familyname=d['Familyname'] )
			if d['Mobile'] != "":
				try:
					Atomic.objects.using(ContactsDB).get( value=d['Mobile'] )
				except:
					Atomic.objects.using(ContactsDB).create( property="Mobile", contact=r.id, type="", value=d['Mobile'] )
			if d['Work'] != "":
				try:
					Atomic.objects.using(ContactsDB).get( value=d['Work'] )
				except:
					Atomic.objects.using(ContactsDB).create( property="Landline", contact=r.id, type="", value=d['Work'] )
			if d['General'] != "":
				try:
					Atomic.objects.using(ContactsDB).get( value=d['General'] )
				except:
					Atomic.objects.using(ContactsDB).create( property="Landline", contact=r.id, type="", value=d['General'] )

	return HttpResponseRedirect(".")

