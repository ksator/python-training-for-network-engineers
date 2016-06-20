#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Retrieve and print the hostname and version of a JUNOS device.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: test_junos_version.py
# -----------------------------------------------------------------------------------------------------------------------
 
from jnpr.junos import Device
ip=raw_input("ip address of the device:") 
login =raw_input("login :") 
pwd=raw_input("passwd:") 
dev=Device(host=ip, user=login, password=pwd)
dev.open()
print "the junos version is " +dev.facts['version']
dev.close()

