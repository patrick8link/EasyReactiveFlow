# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:08:31 2019

@author: Patrick
"""


import putFlow
import createFlow
import time
import delFlow
import checkHost

while True:
    controllerIP = '10.10.1.18'
    if checkHost.checkHost(controllerIP):
        print('New Update')
        createFlow.createFlow()
        delFlow.delFlow(controllerIP,checkHost.countNodes())
        putFlow.putFlow(controllerIP)
        
    time.sleep(10)