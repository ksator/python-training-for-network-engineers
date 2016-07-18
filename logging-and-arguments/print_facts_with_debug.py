#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Connect to a series of devices and print facts related to each device to both the console and an inventory text file.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net

#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: python facts/print_facts_2.py -h
# -----------------------------------------------------------------------------------------------------------------------

from jnpr.junos import Device
from datetime import datetime
import logging
import argparse

parser = argparse.ArgumentParser(description="print hostname of devices not running the expected junos version")

parser.add_argument('-u','--username' ,help='Username required to connect to devices',default="pytraining")
parser.add_argument('-p','--password' ,help='User password to connect to devices',default="Poclab123")
parser.add_argument('-v','--verbose' ,help='Increase verbosity, default=False',action='store_true', default=False)
parser.add_argument('-vv','--very_verbose' ,help='Increase verbosity, default=False',action='store_true', default=False)


options = parser.parse_args()

if options.very_verbose:
    loglevel=logging.DEBUG
elif options.verbose:
    loglevel=logging.INFO
else:
    loglevel=logging.CRITICAL

logging.basicConfig(level=loglevel, filename="logging.txt")


t1 = datetime.now()
mydeviceslist=["172.30.179.101","172.30.179.103", "172.30.179.104", "172.30.179.105"]
print ("size of the list is: " + str(len(mydeviceslist)) + " devices")

f=open("my_devices_inventory.txt", "a")
f.write(str(datetime.now()) + '\n')
for item in mydeviceslist:
        dev=Device(host=item, user=options.username, password=options.password)
        dev.open()
        dev.close()
        if dev.facts["version"]!="12.3R11.2":
           print ("the device "+ dev.facts["hostname"]+ " is a " + dev.facts['model'] + " running " + dev.facts["version"]
)
           f.write ( "the device "+ dev.facts["hostname"]+ " is a " + dev.facts['model'] + " running " + dev.facts["versio
n"] + "\n")
        else:
           print("the device " + dev.facts["hostname"]  + " is checked")
t2 = datetime.now()
t3 = t2-t1
print("done for all devices in " + str(t3) )
f.close()
