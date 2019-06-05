# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:30:43 2019

@author: patri
"""

import putFlow
import createFlow

controllerIP = '10.10.1.18'
createFlow.createFlow()
putFlow.putFlow(controllerIP)