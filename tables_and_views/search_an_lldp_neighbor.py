#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Find neighbors of a specific device using LLDP information retrieved using PyEZ. 
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: search_an_lldp_neighbor.py
# -----------------------------------------------------------------------------------------------------------------------
 
from jnpr.junos import Device
from jnpr.junos.op.lldp import LLDPNeighborTable
import yaml

my_list_of_devices=open('tables_and_views/devices.yml').read()
my_list_of_switches=yaml.load (my_list_of_devices)

neighbor_you_are_looking_for=raw_input("name of the neighbor you are looking for:")

print ("Looking accross the whole network ...")

for element in my_list_of_switches:
	switch = Device(host=element, user='pytraining', password='Poclab123')
	switch.open()
	lldp_neighbors=LLDPNeighborTable(switch)
	lldp_neighbors.get()
	for item in lldp_neighbors:
		if neighbor_you_are_looking_for == item.remote_sysname:
			print ("this neighbor is connected to the interface " +item.local_int + " of the device " + switch.facts["hostname"])
print ("Done")

