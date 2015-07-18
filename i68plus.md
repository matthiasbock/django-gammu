# The SciPhone i68+ #

The SciPhone i68+ is a chinese mobile, looking like the Apple iPhone 3,
but without any restrictions in use, secret movement profiles or silent home calls.
It's a little bit bigger, has a very slow CPU and no GPS.
It's design is less focused on style, more on functionality,
but nevertheless the hardware is clearly cheaper.
The visual effects suck, but it offers clear calls, a long & exchangable battery, Dual-SIM, a slot for Flash memory expansion as well as GPRS internet, a Java Virtual Machine and amazing Bluetooth capabilities.

You can not install Apple iPhone apps on it.
In fact, I'm not sure if there are any apps for it.
But who cares, it runs Java, so maybe it runs Android apps.

# Synchronizing the SciPhone i68+ via Bluetooth #
It is possible to synchronize the phone's contacts via Bluetooth.

## ... using Wammu ##
Wammu does it.
  * Start Wammu
  * Add Phone
  * Automatically search for a Phone
  * Wammu will detect "MTK1 MTK2" via Bluetooth
  * Connect
  * Sync

![http://django-gammu.googlecode.com/svn/trunk/wammu.jpg](http://django-gammu.googlecode.com/svn/trunk/wammu.jpg)

That's it. Very easy, everything works just excellent and took me just a few seconds although I didn't know anything about how to do it :-)

(you may know, that Bluetooth on the Apples iPhone 3 crap doesn't work at all ...)

## ... from the console ##
  * Turn on Bluetooth by clicking the Bluetooth app and "Power On"
  * Turn on your PC's bluetooth device:
```
$ hcitool hci0 up
```
  * Search for the mobile:
```
$ hcitool scan

Scanning ...
	20:E2:05:DE:66:01	MTKBTDEVICE
```
  * Find the bluetooth channel, that serves a SPP:
```
$ sdptool browse 20:E2:05:DE:66:01

Browsing 20:E2:05:DE:66:01 ...
Service Name: Voiceg ateway
Service RecHandle: 0x10000
Service Class ID List:
  "Handsfree Audio Gateway" (0x111f)
  "Generic Audio" (0x1203)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 2
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100
Profile Descriptor List:
  "Handsfree" (0x111e)
    Version: 0x0105

Service Name: AUDIO Gateway
Service RecHandle: 0x10001
Service Class ID List:
  "Headset Audio Gateway" (0x1112)
  "Generic Audio" (0x1203)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 1
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100
Profile Descriptor List:
  "Headset" (0x1108)
    Version: 0x0100

Service Name: Serial Port0
Service RecHandle: 0x10002
Service Class ID List:
  "Serial Port" (0x1101)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 10
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100

Service Name: Dial-up Networking
Service RecHandle: 0x10003
Service Class ID List:
  "Dialup Networking" (0x1103)
  "Generic Networking" (0x1201)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 8
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100
Profile Descriptor List:
  "Dialup Networking" (0x1103)
    Version: 0x0100

Service Name: Advanced Audio
Service RecHandle: 0x10004
Service Class ID List:
  "Audio Source" (0x110a)
Protocol Descriptor List:
  "L2CAP" (0x0100)
    PSM: 25
  "AVDTP" (0x0019)
    uint16: 0x100
Profile Descriptor List:
  "Advanced Audio" (0x110d)
    Version: 0x0100

Service RecHandle: 0x10005
Service Class ID List:
  "AV Remote Target" (0x110c)
Protocol Descriptor List:
  "L2CAP" (0x0100)
    PSM: 23
  "AVCTP" (0x0017)
    uint16: 0x100
Profile Descriptor List:
  "AV Remote" (0x110e)
    Version: 0x0100

Service Name: Human interface device
Service Description: Human interface device
Service Provider: Mediatek Inc
Service RecHandle: 0x10006
Service Class ID List:
  "Human Interface Device" (0x1124)
Protocol Descriptor List:
  "L2CAP" (0x0100)
    PSM: 17
  "HIDP" (0x0011)
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100
Profile Descriptor List:
  "Human Interface Device" (0x1124)
    Version: 0x0100

Service Name: OBEX Object Push
Service RecHandle: 0x10007
Service Class ID List:
  "OBEX Object Push" (0x1105)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 4
  "OBEX" (0x0008)
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100

Service Name: OBEX File Transfer
Service RecHandle: 0x10008
Service Class ID List:
  "OBEX File Transfer" (0x1106)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 3
  "OBEX" (0x0008)
Language Base Attr List:
  code_ISO639: 0x656e
  encoding:    0x6a
  base_offset: 0x100
```
  * as you see, it is channel 10:
```
...
Service Name: Serial Port0
...
  "RFCOMM" (0x0003)
    Channel: 10
...
```
  * connect a radio frequency driven COM port:
```
$ rfcomm0 0 20:E2:05:DE:66:01 10
```
  * your local teletype **/dev/rfcomm0** is now connected and you can use gammu or wammu to sync the phone

  * start wammu

![http://django-gammu.googlecode.com/svn/trunk/SciPhone_Settings.jpg](http://django-gammu.googlecode.com/svn/trunk/SciPhone_Settings.jpg)

## gammu ##

```
 $ rfcomm connect 0 20:E2:05:DE:66:01 10

[gammu]
port = /dev/rfcomm0
model = 
connection = blueat
synchronizetime = yes
logfile = 
logformat = nothing
use_locking = 
gammuloc = 

 $ gammu --config .gammurc getmemory MC 1

Memory MC, Location 1
General number       : "0123456789"
Name                 : "test"
Date and time        : Do 15 Sep 2011 10:20:00 

0 entries empty, 1 entries filled
```

# Synchronization via GPRS #

As far, as I know, it unfortunately doesn't support UMTS, but you can set up
a mobile internet connection via GPRS.

## Setting up a GPRS connection ##
Details follow...

## Synchronizing ##
Details follow...