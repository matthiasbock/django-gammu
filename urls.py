from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
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

	(r'^calendar/$',				"Django.gammu.calendar.index"),
	(r'^calendar/simplelist$',			"Django.gammu.calendar.simplelist"),
	(r'^calendar/listing$',				"Django.gammu.calendar.listing"),
	(r'^calendar/week$',				"Django.gammu.calendar.week"),
	(r'^calendar/month$',				"Django.gammu.calendar.month"),
	(r'^calendar/save$',				"Django.gammu.calendar.save"),

	(r'^calendar/import/$',				"Django.gammu.calendar.import.index"),
	(r'^calendar/export/$',				"Django.gammu.calendar.export.index"),
	(r'^calendar/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/gammu/static', 'show_indexes': True}),
)

