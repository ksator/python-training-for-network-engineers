#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Use PyEZ to enable LLDP on a subset of interfaces for a specific device.
# 
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: enable_lldp.py
# -----------------------------------------------------------------------------------------------------------------------

from jnpr.junos import Device # import the class Device
from jnpr.junos.utils.config import Config # import the class Config
import yaml
s=open('configuration_management/interfaces.yml').read() #s is a string
my_variables=yaml.load(s) # my_variables is a dictionary
a_device=Device (host="172.30.179.113", user="pytraining", password="Poclab123")
a_device.open()
cfg=Config(a_device) # cfg is the candidate configuration
cfg.rollback()
cfg.load(template_path='configuration_management/template_lldp.j2', template_vars=my_variables, format='set')
cfg.pdiff()
cfg.commit()
