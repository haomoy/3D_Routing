# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:42:47 2017

@author: jmper
"""
import adsk.core, adsk.fusion, adsk.cam
import copy 
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
    
    componentNames = []
    CrossHairs = []
    perimeterXs = []
    perimeterYs = []
    componentHeights = []
    Pins = []
    
    '''
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
    '''
    
    for comps in e.iter('Component'):
        currentComponent = comps.get('name')
        #print("Schematic information extractor is exoploring component: ")
        #print(currentComponent)
        #print("###############################################")
        componentNames.append(currentComponent)
        componentHeights.append(comps.get('height'))
        #print("Current component: " + currentComponent)
        
        for pins in comps.iter('Pins'):    
            currentComp = []
            for pin in pins.iter('pin'):
                pininfo = []
                pinname = pin.get('name')
                pinx = pin.get('x')
                piny = pin.get('y')
                pingauge = pin.get('gauge') 
                if(pin.get('length') == "short"):
                    pinlength = str(2.54)
                elif(pin.get('length') == "middle"):
                    pinlength = str(5.08)
                elif(pin.get('length') == "long"):
                    pinlength = str(7.62)
                else:
                    pinlength = str(5.08)
                
                if(pin.get('rot')):
                    pinrot = pin.get('rot')
                else:
                    pinrot = "R0"
                pininfo.append(pinname)
                pininfo.append(pinx)
                pininfo.append(piny)
                pininfo.append(pinlength)
                pininfo.append(pinrot)
                pininfo.append(pingauge)
                pininfo.append(currentComponent)
                currentComp.append(pininfo)
                #print("- " + pinname + ": " + pingauge)
            Pins.append(currentComp)   
    
    for inst in e.iter('Instance'):
        temp = []
        x = inst.get('x')
        y = inst.get('y')
        if(inst.get('rot')):
            r = inst.get('rot')
        else:
            r = "R0"
        temp.append(x)
        temp.append(y)
        temp.append(r)
        CrossHairs.append(temp)
        
    for Perimeter in e.iter('Perimeter'):
        tempX = []
        tempY = []
        for wire in Perimeter.iter('wire'):
            tempX.append(wire.get('x1'))
            tempY.append(wire.get('y1'))
            tempX.append(wire.get('x2'))
            tempY.append(wire.get('y2'))
        perimeterXs.append(tempX)
        perimeterYs.append(tempY)
          
    #ui.messageBox("returning from SIE")
    return componentNames, CrossHairs, perimeterXs, perimeterYs, componentHeights, Pins
            
        
