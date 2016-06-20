#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Merge the variables YML and Jinja2 template to create JUNOS configuration files.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE:
# -----------------------------------------------------------------------------------------------------------------------
import yaml
from jinja2 import Template

f=open('configuration_builder/variables_build.yml')
data=f.read()
my_vars=yaml.load (data)
f.close()
 
f2=open('configuration_builder/template_build.j2')
s2=f2.read()
template=Template(s2)
f2.close()
 
print 'building configuration files ...'
for ex in my_vars:
	print 'generate config file for device '+ex["host_name"]+' : conf_file_build_phase_'+ex["host_name"]+'.conf'
	conffile=open('conf_file_build_phase_'+ex["host_name"]+'.conf','w')
	conffile.write(template.render(ex))
	conffile.close()
print 'done'
 
