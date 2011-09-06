# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Addresses(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact') # Field name made lowercase.
    type = models.CharField(max_length=120, db_column='Type', blank=True) # Field name made lowercase.
    street = models.CharField(max_length=300, db_column='Street') # Field name made lowercase.
    number = models.CharField(max_length=30, db_column='Number') # Field name made lowercase.
    postal = models.CharField(max_length=30, db_column='Postal') # Field name made lowercase.
    city = models.CharField(max_length=90, db_column='City') # Field name made lowercase.
    class Meta:
        db_table = u'Addresses'

class Atoms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    property = models.CharField(max_length=120, db_column='Property') # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact') # Field name made lowercase.
    type = models.CharField(max_length=120, db_column='Type', blank=True) # Field name made lowercase.
    value = models.CharField(max_length=180, db_column='Value') # Field name made lowercase.
    class Meta:
        db_table = u'Atoms'

class Contacts(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner') # Field name made lowercase.
    firstname = models.CharField(max_length=120, db_column='Firstname') # Field name made lowercase.
    familyname = models.CharField(max_length=120, db_column='Familyname') # Field name made lowercase.
    birthday = models.DateField(null=True, db_column='Birthday', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Contacts'

class Gammu(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    manufacturer = models.CharField(max_length=90, db_column='Manufacturer', blank=True) # Field name made lowercase.
    model = models.CharField(max_length=30, db_column='Model', blank=True) # Field name made lowercase.
    connection = models.CharField(max_length=30, db_column='Connection', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Gammu'

class Nicknames(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    nick = models.CharField(max_length=300, db_column='Nick') # Field name made lowercase.
    real = models.CharField(max_length=300, db_column='Real') # Field name made lowercase.
    class Meta:
        db_table = u'Nicknames'

class Users(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    username = models.CharField(max_length=150, db_column='Username') # Field name made lowercase.
    passwordhash = models.CharField(max_length=96, db_column='PasswordHash') # Field name made lowercase.
    class Meta:
        db_table = u'Users'

