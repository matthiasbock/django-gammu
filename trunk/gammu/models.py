# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Contactatoms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact') # Field name made lowercase.
    property = models.CharField(max_length=150, db_column='Property') # Field name made lowercase.
    value = models.CharField(max_length=180, db_column='Value') # Field name made lowercase.
    comment = models.CharField(max_length=300, db_column='Comment') # Field name made lowercase.
    class Meta:
        db_table = u'ContactAtoms'

class Contacts(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner') # Field name made lowercase.
    firstname = models.CharField(max_length=120, db_column='Firstname') # Field name made lowercase.
    surname = models.CharField(max_length=120, db_column='Surname') # Field name made lowercase.
    class Meta:
        db_table = u'Contacts'

class Events(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    start = models.DateTimeField(null=True, db_column='Start', blank=True) # Field name made lowercase.
    end = models.DateTimeField(null=True, db_column='End', blank=True) # Field name made lowercase.
    summary = models.CharField(max_length=765, db_column='Summary', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Events'

class Nicknametable(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    nick = models.CharField(max_length=300, db_column='Nick') # Field name made lowercase.
    real = models.CharField(max_length=300, db_column='Real') # Field name made lowercase.
    class Meta:
        db_table = u'NicknameTable'

class Users(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    username = models.CharField(max_length=150, db_column='Username') # Field name made lowercase.
    passwordhash = models.CharField(max_length=96, db_column='PasswordHash') # Field name made lowercase.
    class Meta:
        db_table = u'Users'

