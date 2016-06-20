#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# List the operational and last flap for all devices in a YAML list.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: uplinks_and_downlinks_last_flap.py
# -----------------------------------------------------------------------------------------------------------------------
 
 
from jnpr.junos.op.phyport import *
from jnpr.junos import Device
from datetime import datetime
import yaml

my_list_of_devices=open('tables_and_views/devices.yml').read()
my_list_of_switches=yaml.load (my_list_of_devices)

f=open("uplinks_and_downlinks_last_flap.txt", "a")
f.write ("\n" + str (datetime.now()) + "\n")

for element in my_list_of_switches:
	switch = Device(host=element, user='pytraining', password='Poclab123')
	switch.open()
	print ("\n" + switch.facts["hostname"] + ":\n")
	f.write ("\n" + switch.facts["hostname"] + ":\n") 
	#print ("\nUplinks and downlinks last flap for " + switch.facts["hostname"] + ":\n")
	#f.write ("\nUplinks and downlinks last flap for " + switch.facts["hostname"] + ":\n")
	ports = PhyPortTable(switch).get()	
	for item in ports:
		if item.description:
			if "LINK" in item.description:
				print (item.key + " (" + item.description + ") " + "current status is " + item.oper + "\n"+ "last flap: " + item.flapped +"\n")
				f.write ("\n" + item.key + " (" + item.description + ") " + "current status is " + item.oper + "\n" + "last flap: " + item.flapped +"\n")	
				#print (item.key + ": " + item.flapped + ". Description is: " + item.description)
				#f.write (item.key + ": " + item.flapped + ". Description is: " + item.description + "\n")
