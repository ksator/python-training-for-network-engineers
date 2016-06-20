#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Use PyEZ to enable LLDP on devices listed in a YAML file.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: enable_lldp_all_devices.py
# -----------------------------------------------------------------------------------------------------------------------
from jnpr.junos import Device # import the class Device
from jnpr.junos.utils.config import Config # import the class Config
import yaml

interface_file_contents = open('configuration_management/interfaces.yml').read() 
interface_variables = yaml.load(interface_file_contents) 

device_file_contents = open('configuration_management/device_list.yml').read()
device_list = yaml.load(device_file_contents)

for device in device_list:
	print device
	dev = Device (host=device, user="pytraining", password="Poclab123")
	dev.open()
	cfg=Config(dev) # cfg is the candidate configuration
	cfg.rollback()
	cfg.load(template_path='configuration_management/template_lldp.j2', template_vars=interface_variables, format='set')
	cfg.pdiff()
	cfg.commit()
