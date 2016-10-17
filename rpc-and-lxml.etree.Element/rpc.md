#RPC discovery method   

##Using cli   
Use "| display xml rpc"  
```
show route protocol isis 10.0.15.0/24 active-path | display xml rpc  
```

##using rpc  
You can fetch the RPC for the show system users CLI command with display_xml_rpc()    
```
>>> r0.display_xml_rpc('show system users')  
<Element get-system-users-information at 0x7fa22b1294d0>  
```
#RPC responses:  

##lxml.etree.Element  
By default, all PyEZ RPC responses are returned as an lxml.etree.Element object.  

###tag  
You can view the actual RPC name by invoking the tag property on this response object  
```
>>> from lxml import etree  
>>> r0.display_xml_rpc('show system users').tag  
'get-system-users-information'  
```
###replace  
You can take this one step further by using the built in replace() string method to substitute hyphens with underscores:  
```
>>> r0.display_xml_rpc('show system users').tag.replace('-','_')  
'get_system_users_information'  
```
#Discover rpc and rpc paramters  
This recipe can be used to discover the RPC name for any Junos CLI command, but does not provide details on an RPC’s parameters.   
Passing the response from the display_xml_rpc() method to the etree.dump() function displays the full XML response (including RPC parameters):  
```
>>> from lxml import etree  
>>> etree.dump(r0.display_xml_rpc('show route protocol isis 10.0.15.0/24 active-path'))  
<get-route-information>  
<destination>10.0.15.0/24</destination>  
<active-path/>  
<protocol>isis</protocol>  
</get-route-information>  
```

#rpc on demand  

With RPC on Demand, there is no tight coupling.  
New features are added to each platform with each Junos release and the existing version of PyEZ can instantly access those RPCs.  
```
>>> isis_route = r0.rpc.get_route_information(protocol='isis', destination='10.0.15.0/24', active_path=True)  
```

#rpc default timeout   
30s  

##first method to change the timeout (for all rpc)  
```
>>> r0.timeout  
30  
>>> r0.timeout = 10  
>>> r0.timeout  
10  
```
##second method (only for one rpc)  
```
>>> bgp_routes = r0.rpc.get_route_information(dev_timeout = 180, protocol='bgp')  
```
#RPC Responses  

PyEZ responses is an lxml.etree.Element  
```
>>> response = r0.rpc.get_system_users_information(normalize=True)  
```
Each lxml.etree.Element object has links to parent, child, and sibling lxml.etree.   
Element objects, which form a tree representing the parsed XML response.    

##lxml.etree.dump()  
For debugging purposes, the lxml.etree.dump() function can be used to dump the XML text of the response (albeit without the pretty formatting of the Junos CLI):  
```
>>> from lxml import etree  
>>> etree.dump(response)  
<system-users-information>  
<uptime-information>  
...ouput trimmed...  
</uptime-information>  
</system-users-information>  
>>>  
```
#convert  lxml.etree.Element object to string (with etree.tostring)   

##Rpc call  

https://github.com/vnitinv/pyez-examples/blob/master/2_rpc_call.py  

```
from jnpr.junos import Device  
from lxml import etree  
dev = Device(host='xxxx', user='demo', password='demo123', gather_facts=False)  
dev.open()  
op = dev.rpc.get_interface_information()  
#op = dev.rpc.get_interface_information(interface_name='lo0', terse=True)  
print (etree.tostring(op))  
dev.close()  
```

##get_config in xml  

https://github.com/vnitinv/pyez-examples/blob/master/10_get_config.py  

```
from jnpr.junos import Device  
from lxml import etree  
dev = Device(host='xxxx', user='demo', password='demo123', gather_facts=False)  
dev.open()  
cnf = dev.rpc.get_config()  
print etree.tostring(cnf)  
```

### example:    

```
>>> from jnpr.junos import Device  
>>> dev=Device(host="172.30.179.101", user="pytraining", password="Poclab123")    
>>> dev.open()  
Device(172.30.179.101)  
>>> rsp=dev.rpc.get_configuration()  
>>> type(rsp)  
<type 'lxml.etree._Element'>  
>>> from lxml import etree  
>>> etree.dump(rsp)  
...  
>>> print etree.tostring(rsp)  
...  
```

##Print diff with rollback id  

```
from jnpr.junos import Device     
from lxml import etree  
dev=Device(host="172.30.177.170", user=xxx, password=xxx)    
dev.open()  
rsp = dev.rpc.get_configuration(dict(compare='rollback', rollback='0', format='xml'))  
print etree.tostring(rsp)  
```

```
>>> print etree.tostring(rsp)  
<configuration-information>  
<configuration-output>  
[edit services analytics resource]    
+...interfaces {    
+.....ge-1/0/0 {    
+.......resource-profile default_resource_profile;  
+.....}  
+.....ge-1/0/1 {    
+.......resource-profile default_resource_profile;    
+.....}    
+...}    
```

## In set format  

Requirement: junos 15.1 or above  
```
from jnpr.junos import Device  
from lxml import etree  
dev=Device(host="172.30.177.170", user=pytraining, password=Poclab123)    
dev.open()  
cnf = dev.rpc.get_configuration(dict(format="set"))  
type(cnf)  
cnf.text  
print cnf.text  
```

#Using XPath with lxml  

```
user@r0> show system users | display xml rpc  
```
```
user@r0> show system users | display xml  
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/15.1R1/junos">  
.<system-users-information xmlns="http://xml.juniper.net/junos/15.1R1/junos">  
..<uptime-information>  
...<date-time junos:seconds="1436915514">4:11PM\</date-time>  
...<up-time junos:seconds="116940">1 day, 8:29\</up-time>  
...<active-user-count junos:format="4 users">4\</active-user-count>  
...<load-average-1>0.56\</load-average-1>  
...  
```
```
>>> response = r0.rpc.get_system_users_information(normalize=True)  
```
##findtext()  

findtext()  method returns a string  
```
>>> response.findtext("uptime-information/up-time")  
'1 day, 8:29'  
```
The <up-time> element also contains a seconds attribute that provides the system’s uptime in seconds since the system booted  

##find() 

While the findtext() method returns a string, the find() method returns an lxml.etree.Element object.  
The XML attributes of that lxml.etree.Element object can then be accessed using the attrib dictionary  
```
>>> response.find("uptime-information/up-time").attrib['seconds']  
'116940'  
```
##findall()  
The findall() method returns a list of lxml.etree.Element objects matching an XPath  
```
>>> users = response.findall("uptime-information/user-table/user-entry/user")  
>>> for user in users:  
... print user.text  
...  
root  
foo  
bar  
user  
>>>  
```
The result of this example is a list of usernames for all users currently logged into the Junos device.  

##Response Normalization  

alter the XML content returned from an RPC method  
When response normalization is enabled, all whitespace characters at the beginning and end of each XML element’s value are removed.   
Response normalization is disabled by default  

```
>>> response = r0.rpc.get_system_users_information()  
>>> response.findtext("uptime-information/up-time")  
'\n4 days, 17 mins\n'  
```
```
>>> response = r0.rpc.get_system_users_information(normalize=True)  
>>> response.findtext("uptime-information/up-time")  
'4 days, 17 mins'  
```

Notice the newline characters at the beginning and end of the value have been removed  
