#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Use PyEZ to automatically merge a variables YML file and a Jinja2 template and update the candidate configuration on
# a device.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: conf_int_with_vlan.py 
# -----------------------------------------------------------------------------------------------------------------------
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml
ip=raw_input("ip address of the device:") 
a_device=Device (host=ip, user="pytraining", password="Poclab123")
a_device.open()
cfg = Config(a_device)
cfg.rollback()
s=open('configuration_management/list_int_vlan.yml').read()
myvars=yaml.load(s)
cfg.load(template_path='configuration_management/template_int_vlan.j2', template_vars=myvars, format='set')
cfg.pdiff()
#cfg.commit()
cfg.rollback()
