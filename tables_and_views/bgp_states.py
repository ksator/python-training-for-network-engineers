#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Print a list of BGP neighbor states for each device in a YAML file using PyEZ.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: bgp_state.py
# -----------------------------------------------------------------------------------------------------------------------
 
 
from jnpr.junos import Device
from jnpr.junos.op.bgp import *
import yaml
from datetime import datetime

f=open("bgp_states.txt", "a")

f.write ("\n" + str (datetime.now()) + "\n")

my_list_of_devices=open('tables_and_views/devices.yml').read()
my_list_of_switches=yaml.load (my_list_of_devices)

for element in my_list_of_switches:
	switch = Device(host=element, user='pytraining', password='Poclab123')
	switch.open()
	bgp=BGPNeighborTable (switch)
	bgp.get()
	print "\nstatus of BGP neighbors of device " + element + " (hostname is " + switch.facts["hostname"]+ "):"
	f.write ("\nstatus of BGP neighbors of device " + element + " (hostname is " + switch.facts["hostname"]+ "):\n")
	for item in bgp:
		print item.type + " BGP neighbor " + item.neighbor + " is " + item.state + " (flap count is: " + item.flap_count +")" 
		f.write (item.type + " BGP neighbor " + item.neighbor + " is " + item.state + " (flap count is: " + item.flap_count + ")\n")

f.close()
