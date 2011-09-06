# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Events(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    start = models.DateTimeField(null=True, db_column='Start', blank=True) # Field name made lowercase.
    end = models.DateTimeField(null=True, db_column='End', blank=True) # Field name made lowercase.
    summary = models.CharField(max_length=765, db_column='Summary', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Events'

