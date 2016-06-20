#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Print a list of non-established BGP connections using PyEZ for each device in a YAML file.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: bgp_non_established.py
# -----------------------------------------------------------------------------------------------------------------------
 
 
from jnpr.junos import Device
from jnpr.junos.op.bgp import *
import yaml
from datetime import datetime

f=open("bgp_neighbors_non_established.txt", "a")

f.write ("\n" + str (datetime.now()) + "\n")

my_list_of_devices=open('tables_and_views/devices.yml').read()
my_list_of_switches=yaml.load (my_list_of_devices)

for element in my_list_of_switches:
	switch = Device(host=element, user='pytraining', password='Poclab123')
	switch.open()
	bgp=BGPNeighborTable (switch)
	bgp.get()
	print "\n" + element + " (hostname " + switch.facts["hostname"]+ ") has these BGP neighbors with a non established connection:"
	f.write ("\n" + element + " (hostname " + switch.facts["hostname"]+ ") has these BGP neighbors with a non established connection:\n")
	for item in bgp:
		if item.state != "Established":
			print item.type + " bgp session with " + item.neighbor + " is not established"
			f.write (item.type + " bgp session with " + item.neighbor + " is not established\n")
print "\ntest done accross all the devices and all their configured neighbors."

f.close()

