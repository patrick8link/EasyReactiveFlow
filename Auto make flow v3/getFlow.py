# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:29:13 2019

@author: patri
"""

import requests
import json

from requests.auth import HTTPBasicAuth #Mengambil fungsi HTTPBasicAuth dari requests

controllerIP = '10.10.1.18'
#URL untuk REST get
URL = 'http://'+controllerIP+':8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1'

response = requests.get(URL, auth = HTTPBasicAuth('admin','admin'))

print(response.status_code)

response.json()

with open('getFlowData.json','w') as outfile:
    json.dump(response.json(),outfile,sort_keys=True,indent=4) 
    