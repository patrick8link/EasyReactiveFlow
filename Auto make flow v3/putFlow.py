# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:51:10 2019

@author: Patrick
"""

import requests
import os
import json

from requests.auth import HTTPBasicAuth #Mengambil fungsi HTTPBasicAuth dari requests

def putFlow(controllerIP):

    with open('dataNodesNew.json') as fh:
        data = json.load(fh)
    
    countNodes = len(data['nodes']['node'])
    
    #static FLOW
    for nodes in range (1,countNodes):
        payload = {'some':'data'}
        headersDel = {'content-type': 'application/xml'}
        delUrl = "http://"+controllerIP+":8181/restconf/config/opendaylight-inventory:nodes/node/openflow:"+str(nodes)
        response = requests.delete(delUrl, data=json.dumps(payload), headers=headersDel,auth=HTTPBasicAuth('admin','admin'))
        print(response.status_code)
        
    #URL untuk REST put
    for nodes in range (0,countNodes):
        
        nodeID = data['nodes']['node'][nodes]['id']
    
        countNodeConnected = len(data['nodes']['node'][nodes]['node-connector'])
        nodeIDName = nodeID.replace('openflow:','S')
        
        idNum = 0
        
        for x in range (90,93):
            putURLStatic = 'http://'+controllerIP+':8181/restconf/config/opendaylight-inventory:nodes/node/'+nodeID+'/table/0/flow/'+str(x)
            dataFlowS = 'dataFlowS'+str(x)+'.json'
            headers = {'Accept':'application/json','Content-type':'application/json'}
            with open(dataFlowS) as fh:
                mydata = fh.read()
                responsePut = requests.put(putURLStatic,
                                           data=mydata,
                                           auth=HTTPBasicAuth('admin','admin'),
                                           headers=headers,
                                           )
                print(responsePut.status_code)
            
        putURLStatic= 'http://'+controllerIP+':8181/restconf/config/opendaylight-inventory:nodes/node/'+nodeID+'/table/1/flow/9999'
        dataFlowS= 'dataFlowS9999.json'
        headers = {'Accept':'application/json','Content-type':'application/json'}
        with open(dataFlowS) as fh:
            mydata = fh.read()
            responsePut = requests.put(putURLStatic,
                                       data=mydata,
                                       auth=HTTPBasicAuth('admin','admin'),
                                       headers=headers,
                                       )
            print(responsePut.status_code)
        
        for x in range (0,countNodeConnected):
            connectorConfiguration = data['nodes']['node'][nodes]['node-connector'][x]['flow-node-inventory:configuration']
            if (connectorConfiguration != 'PORT-DOWN'):
                if ('address-tracker:addresses' in data['nodes']['node'][nodes]['node-connector'][x]):
                    countAddress = len(data['nodes']['node'][nodes]['node-connector'][x]['address-tracker:addresses'])
                    for address in range (0,countAddress):
                        putURL = 'http://'+controllerIP+':8181/restconf/config/opendaylight-inventory:nodes/node/'+nodeID+'/table/2/flow/'+str(idNum)
                        putURL1 = 'http://'+controllerIP+':8181/restconf/config/opendaylight-inventory:nodes/node/'+nodeID+'/table/1/flow/'+str(idNum)
                        putURL2 = 'http://'+controllerIP+':8181/restconf/config/opendaylight-inventory:nodes/node/'+nodeID+'/table/3/flow/'+str(idNum)
                        putURL5 = 'http://'+controllerIP+':8181/restconf/config/opendaylight-inventory:nodes/node/'+nodeID+'/table/4/flow/'+str(idNum)
                        
                        dataFlow = 'dataFlowIP/dataFlowIP'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json'
                        dataFlow1 = 'dataFlowARP/dataFlowARP'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json'
                        dataFlow2 = 'dataFlowARPTable3/dataFlowARPTable3'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json'
                        dataFlow5 = 'dataFlowARPGw/dataFlowARPGw'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json'
                        
                        headers = {'Accept':'application/json','Content-type':'application/json'}
                        
                        checkPut = False
                        
                        if (os.path.isfile(dataFlow)):
                            with open(dataFlow) as fh:
                                mydata = fh.read()
                                responsePut = requests.put(putURL,
                                                           data=mydata,
                                                           auth=HTTPBasicAuth('admin','admin'),
                                                           headers=headers,
                                                           )
                                print('dataFlowIP'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json : '+str(responsePut.status_code)+' - idNum: '+str(idNum))
                                checkPut = True
                                
                        if (os.path.isfile(dataFlow1)):
                            with open(dataFlow1) as fh:
                                mydata = fh.read()
                                responsePut = requests.put(putURL1,
                                                           data=mydata,
                                                           auth=HTTPBasicAuth('admin','admin'),
                                                           headers=headers,
                                                           )
                                print('dataFlowARP'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json : '+str(responsePut.status_code)+' - idNum: '+str(idNum))
                                checkPut = True
                            
                        if (os.path.isfile(dataFlow2)):
                            with open(dataFlow2) as fh:
                                mydata = fh.read()
                                responsePut = requests.put(putURL2,
                                                           data=mydata,
                                                           auth=HTTPBasicAuth('admin','admin'),
                                                           headers=headers,
                                                           )
                                print('dataFlowARPTable3'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json : '+str(responsePut.status_code)+' - idNum: '+str(idNum))
                                checkPut = True
                                                        
                        if (os.path.isfile(dataFlow5)):
                            with open(dataFlow5) as fh:
                                mydata = fh.read()
                                responsePut = requests.put(putURL5,
                                                           data=mydata,
                                                           auth=HTTPBasicAuth('admin','admin'),
                                                           headers=headers,
                                                           )
                                print('dataFlowARPGw'+nodeIDName+'-'+str(x)+'-'+str(address)+'.json : '+str(responsePut.status_code)+' - idNum: '+str(idNum))
                                checkPut = True
                                
                        if (checkPut):
                            idNum=idNum+1