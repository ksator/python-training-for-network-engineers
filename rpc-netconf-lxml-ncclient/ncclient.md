## What is it? 
NetConf client implementation in Python  
Github https://github.com/ncclient/ncclient    
PyPI (Python Package Index) https://pypi.python.org/pypi/ncclient  

## Connect to a device
```
from ncclient import manager
dev=manager.connect(host="ex4200-10", port=830, username="pytraining", password="Poclab123", hostkey_verify=False)
```

## NetConf capabilities

#### print NetConf server capabilities 
```
>>> for item in dev.server_capabilities:
...   print item
...
http://xml.juniper.net/dmi/system/1.0
urn:ietf:params:xml:ns:netconf:capability:confirmed-commit:1.0
urn:ietf:params:xml:ns:netconf:capability:validate:1.0
urn:ietf:params:netconf:capability:validate:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.0
http://xml.juniper.net/netconf/junos/1.0
urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:xml:ns:netconf:capability:candidate:1.0
urn:ietf:params:xml:ns:netconf:capability:url:1.0?protocol=http,ftp,file
urn:ietf:params:xml:ns:netconf:base:1.0
>>>
```
#### check if the server advertised some NetConf capabilities
```
>>> assert(":validate" in dev.server_capabilities), "NetConf server did not advertise the capability :validate"
>>> assert(":candidate" in dev.server_capabilities), "NetConf server did not advertise the capability :candidate"
>>> assert(":confirmed-commit" in dev.server_capabilities), "NetConf server did not advertise the capability :confirmed-commit"
>>>
```

#### print NetConf client capabilities 
```
>>> for item in dev.client_capabilities:
...  print item
...
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:rollback-on-error:1.0
urn:ietf:params:netconf:capability:validate:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file,https,sftp
urn:ietf:params:netconf:base:1.0
urn:liberouter:params:netconf:capability:power-control:1.0
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:netconf:capability:xpath:1.0
urn:ietf:params:netconf:capability:startup:1.0
urn:ietf:params:netconf:capability:interleave:1.0
>>>
```

## backup the active configuration on your labtop
```
f=open ("config", 'w')
f.write(str(dev.get_config(source='running')))
f.close()
```

## print the candidate configuration
```
print dev.get_config(source="candidate")
```

## use a subtree filter to get only interfaces configuration from the active configuration
These 4 examples provide the same output:  
```
criteria='''
<configuration>
	<interfaces>
	</interfaces>
</configuration>
'''
print dev.get_config(source="running", filter=("subtree", criteria))
```
```
criteria2='''
<configuration>
	<interfaces>
</configuration>
'''
print dev.get_config(source="running", filter=("subtree", criteria2))
```
```
criteria3='''
<configuration>
	</interfaces>
</configuration>
'''
print dev.get_config(source="running", filter=("subtree", criteria3))
```
```
criteria4='''
<configuration>
	<interfaces/>
</configuration>
'''
print dev.get_config(source="running", filter=("subtree", criteria4))
```







