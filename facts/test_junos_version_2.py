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
# USAGE: test_junos_version_2.py HOST USER PASSWORD
# -----------------------------------------------------------------------------------------------------------------------
 
from jnpr.junos import Device
import sys
dev=Device (host=sys.argv[1], user=sys.argv[2], password=sys.argv[3])
dev.open()
print ("the device "+ dev.facts["hostname"]+ " runs " + dev.facts["version"])
dev.close()
