#---------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# This script prints the lldp neighbors of the whole network
# it connects to each device (it has the list of devices from a yaml file) and get the lldp neighbors of each device and print some details regarding this.
# it also write the same ouput on a file (ip_fabric_status_of_lldp_neighbors.txt)
#
# AUTHOR:   Khelil SATOR (ksator@juniper.net)
# FILE:     lldp_neighbor_status.py
# CREATED:  2015-10-30
# VERSION: 1
#
# USAGE:
# c:\Python27\IP_FABRIC\audit>lldp_neighbor_status.py
# ---------------------------------------------------------------------------------------------------------------

from jnpr.junos import Device
from jnpr.junos.op.lldp import LLDPNeighborTable
import yaml
from datetime import datetime

my_list_of_devices=open('tables_and_views/devices.yml').read()
my_list_of_switches=yaml.load (my_list_of_devices)

f=open("lldp_neighbors.txt", "a")
f.write ("\n" + str (datetime.now()) + "\n")

for host in my_list_of_switches:
	switch = Device(host=host, user='pytraining', password='Poclab123')
	switch.open()
	print "\nLLDP neighbors of device " + host + " (hostname is " + switch.facts["hostname"]+ "):"
	f.write ("\nLLDP neighbors of device " + host + " (hostname is " + switch.facts["hostname"]+ "):\n")
	lldp_neighbors=LLDPNeighborTable(switch)
	lldp_neighbors.get()
	for neighbor in lldp_neighbors:
		print "interface " + neighbor.local_int + " has this neighbor: " + neighbor.remote_sysname
		f.write ("interface " + neighbor.local_int + " has this neighbor: " + neighbor.remote_sysname + "\n")
f.close()

