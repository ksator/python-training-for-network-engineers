#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Generate configuration files based on variables stored in YML and a Jinja 2 template and apply the configuration
# to the devices.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: configuration_builder.py 
# -----------------------------------------------------------------------------------------------------------------------
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml
from jinja2 import Template

f=open('configuration_builder/variables.yml')
data=f.read()
my_vars=yaml.load (data)

f2=open('configuration_builder/template.j2')
s2=f2.read()
template=Template(s2)

print 'Start configuration building'
for ex in my_vars:
    print 'generate config file for device '+ex["host_name"]+' : conf_file_build_phase_'+ex["host_name"]+'.conf'
    conffile=open('conf_file_build_phase_'+ex["host_name"]+'.conf','w')
    conffile.write(template.render(ex))
    conffile.close()
print 'done'


print 'applying the conf to the devices ...'
for ex in my_vars:
	dev = Device(host=ex["management_ip"], user='pytraining', password='Poclab123')
	dev.open()
	cfg=Config(dev)
	cfg.rollback() # Execute Rollback to prevent commit change from old config session
	#cfg.load(template_path='template_for_ex.j2', template_vars=my_vars, format='text')
	cfg.load(path='conf_file_build_phase_'+ex["host_name"]+'.conf', format='text')
	if cfg.commit() == True:
		print ('configuration commited on ' + dev.facts["hostname"])
	else:
		print ('commit failed on ' + dev.facts["hostname"])
	dev.close()
print ('done')



