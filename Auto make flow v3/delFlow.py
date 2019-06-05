# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:03:27 2019

@author: patri
"""

import requests
import json

from requests.auth import HTTPBasicAuth #Mengambil fungsi HTTPBasicAuth dari requests

controllerIP = '10.10.1.18'

def delFlow(controllerIP,countNodes):
    payload = {'some':'data'}
    headers = {'content-type': 'application/xml'}
    
    for x in range (1,countNodes):
        url = "http://"+controllerIP+":8181/restconf/config/opendaylight-inventory:nodes/node/openflow:"+str(x)+""
        response = requests.delete(url, data=json.dumps(payload), headers=headers,auth=HTTPBasicAuth('admin','admin'))
        print(response.status_code)