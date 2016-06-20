#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Print the hostname and version of a list of devices with connection timeout exception handling.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: exceptions_handling2.py
# -----------------------------------------------------------------------------------------------------------------------

# mydeviceslist is a list of device running junos
# for each device in mydeviceslist, we will connect to the device and print some facts
# if a device is not reacheable, we will print something and continue the program

from jnpr.junos import Device
from jnpr.junos.exception import *
mydeviceslist=["172.30.179.101", "172.30.179.102", "172.30.205.102", "172.30.179.104"]
for item in mydeviceslist:
	dev=Device(host=item, user="pytraining", password="Poclab123")
	try:
		dev.open()
	except ConnectTimeoutError:
		print("failed to connect to " + item)
		continue

	print ("the device "+ item + " runs " + dev.facts["version"])
	dev.close()	
