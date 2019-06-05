# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:56:12 2019

@author: patri
"""
import json
import objectpath

with open('dataNodesNew.json') as new:
    dataNew = json.load(new)
    print ('finish Load New')
        
with open('dataNodesOld.json') as old:
    dataOld = json.load(old)
    print ('finish Load Old')

if ('node' in dataNew['nodes']):
        countNodesNew = len(dataNew['nodes']['node']) #count how many nodes are there
        
        for nodes in range (0,countNodesNew):
            countNodeConnectedNew = len(dataNew['nodes']['node'][nodes]['node-connector'])
            for x in range (0,countNodeConnectedNew):
                if ('address-tracker:addresses' in dataNew['nodes']['node'][nodes]['node-connector'][x]):
                    countAddressNew = len(dataNew['nodes']['node'][nodes]['node-connector'][x]['address-tracker:addresses'])
                    print countAddressNew
                    
                    address = (dataNew['nodes']['node'][nodes]['node-connector'][x]['address-tracker:addresses'])
                    portName = dataNew['nodes']['node'][nodes]['node-connector'][x]['flow-node-inventory:name']
                    
                    jsonnn_tree = objectpath.Tree(dataOld['nodes']['node'][nodes])
                    a="$.'node-connector'[@.'flow-node-inventory:name' is '"+portName+"'].'address-tracker:addresses'"
                    tuplea = list(jsonnn_tree.execute(a))
                    print tuplea
                    if not tuplea:
                        print ("List is empty")
                    else:
                        print len(tuplea[0])
                        print (portName)

