from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	(r'^contacts/$',				"Django.contacts.main.index"),
	(r'^contacts/contacts$',			"Django.contacts.main.Table"),
	(r'^contacts/edit$',				"Django.contacts.main.EditContact"),
	(r'^contacts/remove$',				"Django.contacts.main.RemoveContact"),
	(r'^contacts/addatom$',				"Django.contacts.main.AddAtom"),
	(r'^contacts/removeatom$',			"Django.contacts.main.RemoveAtom"),
	(r'^contacts/synchronize$',			"Django.contacts.sync.index"),
	(r'^contacts/IrDA/attach$',			"Django.contacts.irda.attach"),
	(r'^contacts/IrDA/download$',			"Django.contacts.irda.download"),
	(r'^contacts/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/contacts/static', 'show_indexes': True}),

	(r'^calendar/$',				"Django.gammu.calendar.index"),
	(r'^calendar/listing$',				"Django.gammu.calendar.listing"),
	(r'^calendar/week$',				"Django.gammu.calendar.week"),
	(r'^calendar/month$',				"Django.gammu.calendar.month"),

	(r'^calendar/import/$',				"Django.gammu.calendar.import.index"),
	(r'^calendar/export/$',				"Django.gammu.calendar.export.index"),
	(r'^calendar/static/(?P<path>.*)$',		'django.views.static.serve', {'document_root': '/var/www/Django/calendar/static', 'show_indexes': True}),
)

