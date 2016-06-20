#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Attempt to connect to a device and print the device hostname and version.  Handle all exceptions related to device
# connection.
# 
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: exception_handling.py HOST USERNAME PASSWORD
# -----------------------------------------------------------------------------------------------------------------------
from jnpr.junos import Device
import sys
from jnpr.junos.exception import *
dev=Device (host=sys.argv[1], user=sys.argv[2], password=sys.argv[3])
try:
    dev.open()
except ConnectUnknownHostError:
    print(sys.argv[1] + " is not a valid host!")
except ConnectAuthError:
    print("invalid username or password for host " + sys.argv[1])
except ConnectTimeoutError:
    print("failed to connect to " + sys.argv[1] + ". could be: a bad ip addr, ip addr is not reachable due to a routing issue or a firewall filtering, ...")
except :
    print("another error ...")
else:
    print ("the device "+ dev.facts["hostname"]+ " runs " + dev.facts["version"])   


