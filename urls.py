from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	# Contacts
	(r'^contacts/$',				"Django.gammu.main.index"),
	(r'^contacts/contacts$',			"Django.gammu.contacts.Table"),
	(r'^contacts/edit$',				"Django.gammu.contacts.EditContact"),
	(r'^contacts/remove$',				"Django.gammu.contacts.RemoveContact"),
	(r'^contacts/addatom$',				"Django.gammu.contacts.AddAtom"),
	(r'^contacts/removeatom$',			"Django.gammu.contacts.RemoveAtom"),
	(r'^contacts/synchronize$',			"Django.gammu.contacts.sync"),
	(r'^contacts/IrDA/attach$',			"Django.gammu.contacts.irdaattach"),
	(r'^contacts/IrDA/download$',			"Django.gammu.contacts.irdadownload"),
	(r'^contacts/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/gammu/static', 'show_indexes': True}),

	# Calendar
	(r'^calendar/$',				"Django.gammu.calendar.index"),

	(r'^calendar/simplelist$',			"Django.gammu.calendar.simplelist"),
	(r'^calendar/list$',				"Django.gammu.calendar.advancedlist"),

	(r'^calendar/day$',				"Django.gammu.calendar.day"),
	(r'^calendar/threedays$',			"Django.gammu.calendar.threedays"),
	(r'^calendar/week$',				"Django.gammu.calendar.week"),
	(r'^calendar/month$',				"Django.gammu.calendar.month"),
	(r'^calendar/year$',				"Django.gammu.calendar.year"),

	(r'^calendar/save$',				"Django.gammu.calendar.save"),
	(r'^calendar/delete$',				"Django.gammu.calendar.delete"),

	(r'^calendar/import/$',				"Django.gammu.calendar.import"),
	(r'^calendar/export/$',				"Django.gammu.calendar.export"),

	(r'^calendar/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/gammu/static', 'show_indexes': True}),
)

