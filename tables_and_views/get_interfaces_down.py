#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# List all ports that are operationally down for a device.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: get_interfaces_down.py
# -----------------------------------------------------------------------------------------------------------------------
 
 
from jnpr.junos.op.phyport import *
from jnpr.junos import Device
ip=raw_input("ip address of the device:") 
dev=Device (host=ip, user="pytraining", password="Poclab123")
dev.open()
ports = PhyPortTable(dev).get()
for item in ports:
	if item.oper == "down":
		print ("the port " + item.key + " is down")


