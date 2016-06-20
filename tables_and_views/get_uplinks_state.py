#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Get the state of all interfaces with UPLINK in their description for a device.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: get_uplinks_state.py
# -----------------------------------------------------------------------------------------------------------------------
 
 
from jnpr.junos.op.phyport import *
from jnpr.junos import Device
ip=raw_input("ip address of the device:") 
dev=Device (host=ip, user="pytraining", password="Poclab123")
dev.open()
ports = PhyPortTable(dev).get()
for item in ports:
	if item.description and ( "UPLINK" in item.description):
		print "Uplink " + item.key + " (" + item.description + ") is " + item.oper
