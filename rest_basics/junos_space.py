#extract the ip address of all EX4300-48T from junos space

from pprint import pprint as pp
from requests import get
from requests.auth import HTTPBasicAuth

''' 
https://www.juniper.net/techpubs/en_US/junos-space-sdk/13.3/apiref/com.juniper.junos_space.sdk.help/JSInventoryManagerSVC/Docs/rest.managed-elements.html
'''
url='https://172.30.109.80'
uri=url + '/api/space/managed-domain/managed-elements'
my_headers= {'Accept': 'application/vnd.net.juniper.space.managed-domain.managed-elements+json;version=1'}
r = get(uri, auth=HTTPBasicAuth('super', 'Juniper123'), verify=False, headers=my_headers)

#r.json()['managed-elements']['managed-element'][-1]

#for item in r.json()['managed-elements']['managed-element']:
#    print item[u'ipAddr']

'''
https://www.juniper.net/techpubs/en_US/junos-space-sdk/13.3/apiref/com.juniper.junos_space.sdk.help/JSInventoryManagerSVC/Docs/rest.managed-elements.id.html
'''
my_headers2={'Accept': 'application/vnd.net.juniper.space.managed-domain.managed-element+json;version=1;q=.01'}
for item in r.json()['managed-elements']['managed-element']:
    id = int(item[u'@key'])
    uri = url + "/api/space/managed-domain/managed-elements/"+str(id)
    r2 = get(uri, auth=HTTPBasicAuth('super', 'Juniper123'), verify=False, headers=my_headers2)
    if str(r2.json()['managed-element']['device']['platform'])=="EX4300-48T": 
     print r2.json()['managed-element']['ipAddr']

'''
output is the ip address of EX4300-48T devices in junos space
172.30.108.138
172.30.108.134
'''
