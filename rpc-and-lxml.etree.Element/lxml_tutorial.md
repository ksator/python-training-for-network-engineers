# lxml python package tutorial

### etree module 

###### import the etree module from the the lxml package 
```
>>> from lxml import etree
```

###### Call the Element class
```
>>> root=etree.Element('root')
>>> type(root)
<type 'lxml.etree._Element'>
>>>
```

###### The function tostring returns a string representation of an element
```
>>> etree.tostring(root)
'<root/>'
>>>
```

###### To create child elements and add them to a parent element, you can use the append() method:
```
>>> root.append(etree.Element('child1'))
>>> etree.tostring(root)
'<root><child1/></root>'
>>>
>>> print etree.tostring(root, pretty_print=True)
<root>
  <child1/>
</root>
>>>
```

###### Subelement class creates an element instance, and appends it to an existing element.
```
>>> child2 = etree.SubElement(root, "child2")
>>> child3 = etree.SubElement(root, "child3")
>>> print(etree.tostring(root, pretty_print=True))
<root>
  <child1/>
  <child2/>
  <child3/>
</root>
```

###### the function dump  
```
>>> etree.dump(root)
<root>
  <child1/>
  <child2/>
  <child3/>
</root>
>>> 
```

###### we can handle elements like lists
```
>>>len(root)
3
>>> for item in root:
...     print item
... 
<Element child1 at 0x7fb17dee58c0>
<Element child2 at 0x7fb17dee5e60>
<Element child3 at 0x7fb17dee5950>
>>> for item in root:
...     print item.tag
... 
child1
child2
child3
>>> root[0]
<Element child1 at 0x7f93feee3d40>
>>> root[-1]
<Element child3 at 0x7f93feee3a28>
>>> 
```

###### getparent(), getchildren(), getprevious(), getnext()
we can call getparent(), getchildren(), getprevious(), getnext() to get the parent, children, neigbbors of an element
```
>>> root.getchildren()
[<Element child1 at 0x7f93feee3d40>, <Element child2 at 0x7f93feee3d88>, <Element child3 at 0x7f93feee3a28>]
>>> child2.getprevious()
<Element child1 at 0x7f93feee3d40>
>>> child2.getparent()
<Element root at 0x7f93feee38c0>
>>> child2.getnext()
<Element child3 at 0x7f93feee3a28>
```

###### Elements can contain text:
```
>>> child2.text = 'qwerty'
>>> print child2.text
qwerty
>>> etree.tostring(root)
'<root><child1/><child2>qwerty</child2><child3/></root>'
>>> print etree.tostring(root)
<root><child1/><child2>qwerty</child2><child3/></root>
>>> print etree.tostring(root, pretty_print=True)
<root>
  <child1/>
  <child2>qwerty</child2>
  <child3/>
</root>
>>> etree.SubElement(root, "another").text = "zxcvb"
>>> print etree.tostring(root, pretty_print=True)
<root>
  <child1/>
  <child2>qwerty</child2>
  <child3/>
  <another>zxcvb</another>
</root>
```

### findtext, find, findall 

###### findtext function returns the text for the matching subelement
```
>>> etree.dump(root)
<root>
  <child1/>
  <child2/>
  <child3/>
  <another>zxcvb</another>
</root>
>>> root.findtext('another')
'zxcvb'
>>> 
```
###### find function returns a subelement
```
>>> root.find('another')
<Element another at 0x7f9401e82710>
>>> root.find('another').text
'zxcvb'
>>> 
```

###### findall function returns a list of subelements
```
>>> etree.SubElement(root, "another").text = "advcrwvc"
>>> etree.SubElement(root, "another").text = "vfet"
>>> etree.dump(root)
<root>
  <child1/>
  <child2/>
  <child3/>
  <another>zxcvb</another>
  <another>advcrwvc</another>
  <another>vfet</another>
</root>
>>> root.findall('another')
[<Element another at 0x7f93feef5c20>, <Element another at 0x7f93feef57e8>, <Element another at 0x7f93fede65f0>]
>>> for item in root.findall('another'):
...  print item.text
... 
zxcvb
advcrwvc
vfet
>>>
```

### builder module 

####### Import the class E (aka ElementMaker) from the module lxml.builder
```
>>> from lxml.builder import E
```
###### Call the class E 
```
>>> rpc = E('root', E('child1'))
>>> type(rpc)
<type 'lxml.etree._Element'>
>>> print(etree.tostring(rpc, pretty_print=True))
<root>
  <child1/>
</root>
>>> rpc = E('root', E('child1', 'blabla'))
>>> print(etree.tostring(rpc, pretty_print=True))
<root>
  <child1>blabla</child1>
</root>
>>> from lxml.builder import E
>>> rpc = E('get', E('filter', {'type': 'xpath', 'source': '/bgp'}))
>>> type(rpc)
<type 'lxml.etree._Element'>
>>> etree.tostring(rpc)
'<get><filter source="/bgp" type="xpath"/></get>'
>>> print(etree.tostring(rpc, pretty_print=True))
<get>
  <filter source="/bgp" type="xpath"/>
</get>
```

