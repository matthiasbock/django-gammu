# How to dial a number without touching the phone #

In order to dial a number on your phone,
you need a _Dial-Up-Networking_ connection to it.
You may establish it via pluggin your phone in (USB) or via Bluetooth.

## Bluetooth ##

  * Let's say, you have enabled Bluetooth on your [SciPhone](SciPhone_i68plus.md) and the _Dial-Up-Networking_ channel is 8:
```
$ sdptool browse 20:E2:05:DE:66:01

Service Name: Dial-up Networking
Service RecHandle: 0x10003
Service Class ID List:
  "Dialup Networking" (0x1103)
  "Generic Networking" (0x1201)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 8
```
  * connect Bluetooth channel 8 to local radio frequency port 0 (/dev/rfcomm0):
```
$ rfcomm connect 0 20:E2:05:DE:66:01 8
```
  * the AT command to dial the number 123456789 is:
```
 ATD 123456789
```
  * send it to the phone:
```
echo "ATD 123456789" > /dev/rfcomm0
```
  * now it should dial the number