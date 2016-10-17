## What is it? 
NetConf client implementation in Python  
Github https://github.com/ncclient/ncclient    
PyPI (Python Package Index) https://pypi.python.org/pypi/ncclient  

## Connect to a device
```
>>> from ncclient import manager
>>> dev=manager.connect(host="ex4200-10", port=830, username="pytraining", password="Poclab123", hostkey_verify=False)
>>> dev.connected
True
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

## get_config 

#### backup the active configuration on your labtop
```
f=open ("config", 'w')
f.write(str(dev.get_config(source='running')))
f.close()
```

#### print the candidate configuration
```
print dev.get_config(source="candidate")
```

#### use a subtree filter to get only interfaces configuration from the active configuration
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

## Update the candidate configuration, and commit
```
print 'locking configuration'
dev.lock('candidate')
snippet='''<config><configuration><system><host-name operation="replace">newname</host-name></system></configuration></config>'''
dev.edit_config(target='candidate', config=snippet)
dev.commit()
dev.unlock('candidate')
```

## Revert the candidate configuration to the currently running configuration.

#### Update the candidat configuration 
```
snippet='''<config><configuration><system><host-name operation="replace">anothername</host-name></system></configuration></config>'''
dev.edit_config(target='candidate', config=snippet)
```

###### Get the candidate configuration  
```
>>> criteria='''
... <configuration>
...   <system>
...     <host-name>
...   </system>
... </configuration>
... '''
>>> print dev.get_config(source="candidate", filter=("subtree", criteria))
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:junos="http://xml.juniper.net/junos/12.3R11/junos" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:87796708-9463-11e6-a102-005056ab0085">
<data>
<configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm" junos:changed-seconds="1476706420" junos:changed-localtime="2016-10-17 14:13:40 CEST">
    <system>
        <host-name>anothername</host-name>
    </system>
</configuration>
</data>
</rpc-reply>
```

###### Revert the candidate configuration to the currently running configuration.
Any uncommitted changes are discarded.
```
>>> dev.discard_changes()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:junos="http://xml.juniper.net/junos/12.3R11/junos" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:aa089de8-9463-11e6-a102-005056ab0085">
<ok/>
</rpc-reply>
```
###### Check the candidate configuration 
```
>>> print dev.get_config(source="candidate", filter=("subtree", criteria))
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:junos="http://xml.juniper.net/junos/12.3R11/junos" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:abe8fa9a-9463-11e6-a102-005056ab0085">
<data>
<configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm" junos:changed-seconds="1476706602" junos:changed-localtime="2016-10-17 14:16:42 CEST">
    <system>
        <host-name>ex4200-10</host-name>
    </system>
</configuration>
</data>
</rpc-reply>
>>>
```

## Close the NetConf session

```
>>> dev.connected
True
>>> dev.close_session()
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:junos="http://xml.juniper.net/junos/12.3R11/junos" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:956c0756-94b0-11e6-8523-005056ab0085">
<ok/>
</rpc-reply>
>>>
>>> dev.connected
False
```

## device handlers
if you add device_params={'name':'junos'} as an argument of the class connect, you can even better manage Junos devices. 
Few examples:  
- you can call the method commit with the argument comment: commit(comment="from ncclient")   
- you can use an xpath despite Junos device does not advertise the NetConf capability :xpath  

#### Commit comment 
```
from ncclient import manager
dev=manager.connect(host="ex4200-10", port=830, username="pytraining", password="Poclab123", hostkey_verify=False, device_params={'name':'junos'})
dev.lock('candidate')
snippet='''<config><configuration><system><host-name operation="replace">newname</host-name></system></configuration></config>'''
dev.edit_config(target='candidate', config=snippet)
dev.commit(comment="from ncclient")
dev.unlock('candidate')
```

#### xpath 
```
ttt=dev.get()
print ttt
```
```
>>> ttt.xpath('//name-server/name')
[<Element name at 0x7f19cc876830>, <Element name at 0x7f19cc876950>]
>>> type(ttt.xpath('//name-server/name'))
<type 'list'>
>>> len(ttt.xpath('//name-server/name'))
2
>>> ttt.xpath('//name-server/name')[0]
<Element name at 0x7f19cc876830>
>>> ttt.xpath('//name-server/name')[0].text
'172.30.179.2'
>>> ttt.xpath('//name-server/name')[1].text
'172.30.179.3'
>>> for item in ttt.xpath('//name-server/name'):
...  print item
...
<Element name at 0x7f5c71da0560>
<Element name at 0x7f5c71da0518>

>>> for item in ttt.xpath('//name-server/name'):
...  print item.text
...
172.30.179.2
172.30.179.3
>>>

>>> from lxml import etree
>>> for item in ttt.xpath('//name-server/name'):
...  print etree.tostring(item)
...
<name>172.30.179.2</name>

<name>172.30.179.3</name>

>>>
```





