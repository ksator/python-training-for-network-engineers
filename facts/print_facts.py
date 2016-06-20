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
# USAGE: print_facts.py
# -----------------------------------------------------------------------------------------------------------------------
 
from jnpr.junos import Device
from datetime import datetime

mydeviceslist=["172.30.179.103", "172.30.179.104", "172.30.179.105"]
f=open("my_devices_inventory.txt", "a")
f.write(str(datetime.now()) + '\n')
for item in mydeviceslist:
	dev=Device(host=item, user="pytraining", password="Poclab123")
	dev.open()
        dev.close()
        if dev.facts["version"]!="15.1":  
         print ("the device "+ dev.facts["hostname"]+ " is a " + dev.facts['model'] + " running " + dev.facts["version"])
	 f.write ( "the device "+ dev.facts["hostname"]+ " is a " + dev.facts['model'] + " running " + dev.facts["version"] + "\n")
f.close()

