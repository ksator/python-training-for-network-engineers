#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Connect to a series of devices and print facts related to each device to both the console and an inventory text file.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: python facts/print_facts_3.py -h
# -----------------------------------------------------------------------------------------------------------------------

from jnpr.junos import Device
from datetime import datetime
import logging
import argparse

parser = argparse.ArgumentParser(description="print hostname of devices not running the expected junos version")
parser.add_argument('-u','--username' ,help='Username required to connect to devices',default="pytraining")
parser.add_argument('-p','--password' ,help='User password to connect to devices',default="Poclab123")
parser.add_argument("--log", default='info', choices=['info', 'warn', 'debug', 'error'], help="Specify the log level")

# create logger
logger = logging.getLogger( 'facts' )

# specifies the severity the logger will handle
options = parser.parse_args()
if options.log == 'debug':
    logger.setLevel(logging.DEBUG)
elif options.log == 'warn':
    logger.setLevel(logging.WARN)
elif options.log == 'error':
    logger.setLevel(logging.ERROR)
else:
    logger.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create a console handler
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)

# add a handler to the logger object
logger.addHandler(steam_handler)

# create a handler
file_handler = logging.FileHandler("facts.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add the handler to logger
logger.addHandler(file_handler)

# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

t1 = datetime.now()
mydeviceslist=["172.30.179.101","172.30.179.103", "172.30.179.104", "172.30.179.105"]
logger.debug ("size of the list is: " + str(len(mydeviceslist)) + " devices")

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
           logger.debug("the device " + dev.facts["hostname"]  + " is checked")
t2 = datetime.now()
t3 = t2-t1
print("done for all devices in " + str(t3) )
f.close()
