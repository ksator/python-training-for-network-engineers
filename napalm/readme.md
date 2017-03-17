NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library to interact with different network operating systems.  
source code: https://github.com/napalm-automation/napalm  
doc: https://napalm.readthedocs.io/en/latest/index.html  
installation:  
```
sudo pip install napalm

```
Usages:
you can use napalm into a python script or as a cli tool.  
into a python script:  
```
ksator@ubuntu:~$ more conf.txt 
system {
    host-name newhostname;
    }
```
```
ksator@ubuntu:~$ python
>>> import napalm
>>> driver = napalm.get_network_driver('junos')
>>> device = driver(hostname='172.30.179.107', username='pytraining', password='Poclab123', optional_args={'port': 830})
>>> device.open()
>>> from pprint import pprint as pp
>>> pp(device.get_facts())
{u'fqdn': u'newname.poc-nl.jnpr.net',
 u'hostname': u'newname',
 u'interface_list': ['ge-0/0/0',
                     'ge-0/0/1',
                     'ge-0/0/2',
                     'ge-0/0/3',
                     'ge-0/0/4',
                     'ge-0/0/5',
                     'ge-0/0/6',
                     'ge-0/0/7',
                     'ge-0/0/8',
                     'ge-0/0/9',
                     'ge-0/0/10',
                     'ge-0/0/11',
                     'ge-0/0/12',
                     'ge-0/0/13',
                     'ge-0/0/14',
                     'ge-0/0/15',
                     'ge-0/0/16',
                     'ge-0/0/17',
                     'ge-0/0/18',
                     'ge-0/0/19',
                     'ge-0/0/20',
                     'ge-0/0/21',
                     'ge-0/0/22',
                     'ge-0/0/23',
                     'ge-0/0/24',
                     'ge-0/0/25',
                     'ge-0/0/26',
                     'ge-0/0/27',
                     'ge-0/0/28',
                     'ge-0/0/29',
                     'ge-0/0/30',
                     'ge-0/0/31',
                     'ge-0/0/32',
                     'ge-0/0/33',
                     'ge-0/0/34',
                     'ge-0/0/35',
                     'ge-0/0/36',
                     'ge-0/0/37',
                     'ge-0/0/38',
                     'ge-0/0/39',
                     'ge-0/0/40',
                     'ge-0/0/41',
                     'ge-0/0/42',
                     'ge-0/0/43',
                     'ge-0/0/44',
                     'ge-0/0/45',
                     'ge-0/0/46',
                     'ge-0/0/47',
                     '.local.',
                     'vcp-0',
                     'vcp-1',
                     'bme0',
                     'dsc',
                     'gre',
                     'ipip',
                     'lo0',
                     'lsi',
                     'me0',
                     'mtun',
                     'pimd',
                     'pime',
                     'tap',
                     'vlan',
                     'vme'],
 u'model': u'EX4200-48T',
 u'os_version': u'12.3R11.2',
 u'serial_number': u'BP0208111225',
 u'uptime': 15827760,
 u'vendor': u'Juniper'}
>>> 
>>> device.load_merge_candidate(filename='conf.txt')
>>> device.compare_config()
'[edit system]\n-  host-name newname;\n+  host-name newhostname;'
>>> device.rollback()
>>>
>>> device.is_alive()
{u'is_alive': True}
>>>
>>> device.close()
>>> device.is_alive()
{u'is_alive': False}
>>>
>>> exit()
```
You can use napalm cli tool:  

to get the help, run this command:  
```
cl_napalm_configure --help
```
Example with dry run:
```
ksator@ubuntu:~$ cl_napalm_configure --user pytraining --vendor junos --strategy merge --dry-run 172.30.177.170 napalm/conf.txt 
Enter password: 
[edit system]
-  host-name mx80-17;
+  host-name newhostname;
ksator@ubuntu:~$ 
```



