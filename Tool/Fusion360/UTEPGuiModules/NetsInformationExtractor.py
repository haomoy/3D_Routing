# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:42:47 2017

@author: jmper
"""
import adsk.core, adsk.fusion, adsk.cam
from xml.etree import ElementTree as ET
global app
global ui
app = adsk.core.Application.get()
ui = app.userInterface

def run(directory, filename):
    ##print("_________________________________________________________")
    dirName = directory#os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    dirname = dirName + filename[:len(filename)-4] + "_outputXML.xml"
    #dirname = dirname.replace("/", "\\")
    e = ET.parse(dirname)
    
    Nets = []
       
    for nets in e.iter('Nets'):
        for net in nets.iter('Net'):
            currentNet = []
            NetName = net.get('name')
            #print("Net name is: "+NetName)
            for pin in net.iter('Pin'):
                Currentpin = []
                pinName = pin.get('name')
                pinComp = pin.get('component')
                #print("Pin name is: "+pinName+", component is: "+pinComp)
                Currentpin.append(NetName)
                Currentpin.append(pinName)
                Currentpin.append(pinComp)
                currentNet.append(Currentpin)
            Nets.append(currentNet)

    return Nets
            
        