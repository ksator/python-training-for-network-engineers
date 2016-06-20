#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Retrieve software information from an MX router with a REST API call.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: get_mx_software_information.py
# -----------------------------------------------------------------------------------------------------------------------
 
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

my_headers = { 'Accept': 'application/json' }

r = requests.get('http://172.30.177.170:3000/rpc/get-software-information', auth=HTTPBasicAuth('pytraining', 'Poclab123'), headers=my_headers)

#pprint(r.json())
print "Software version: " + r.json()['software-information'][0]['junos-version'][0]['data']
print "Host-name: " + r.json()['software-information'][0]['host-name'][0]['data']
print "Product name: " + r.json()['software-information'][0]['product-name'][0]['data']
