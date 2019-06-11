import adsk.core, adsk.fusion, traceback
import ctypes
import math
import re

def run(context, file_name, pin_extension, Nets, Components):
    ui = None
    try:
        global app 
        app = adsk.core.Application.get()
        global ui
        ui = app.userInterface
        global fileName
        fileName = filename
        global pinExtension
        pinExtension = extension/10.0 #converting from cm to mm
        Nets = Ns
        
        sketches()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
            
def sketches():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        global temp
        global lastx
        global lasty
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        plane = selectedPlane.geometry.origin
        modelface = selectedPlane.component
        model = modelface.bRepBodies.item(0)
        x = model.boundingBox.minPoint.x + 1.0
        z = (plane.y)
        #y = -(plane.z)
        y = -model.boundingBox.minPoint.z - 1.0
        
        
        CompNames = []
        CompHeights = []
        Pins = []
        Crosshairs = []
        XCords = []
        YCords = []
        
        smallestX = float("inf")
        smallestY = float("inf")
        smallestIndex = 0
        #ORDERING THEM AS THEY SHOW UP FROM LEFT TO RIGHT. LEFT-MOST = FIRST, RIGHT-MOST = LAST.
        length = len(Cross)
        for g in range(0, length):
            #print("g is: "+str(g))
            tempsmallestX = float("inf")
            tempsmallestIndex = 0
            for h in range(0, len(Cross)):
                if( float(Cross[h][0])/10.0 < tempsmallestX ):
                    #print("entered if statement with Cross[h][0] = "+str(Cross[h][0])+", and smallest = "+str(smallestX))
                    tempsmallestX = float(Cross[h][0])/10.0
                    tempsmallestIndex = h
                    if(tempsmallestX < smallestX):
                        smallestX = tempsmallestX
                        smallestIndex = h
#                if(float(Cross[h][1])/10.0 < smallestY):
#                    smallestY = float(Cross[h][1])/10.0
            CompNames.append(CNames.pop(tempsmallestIndex))
            CompHeights.append(CHeights.pop(tempsmallestIndex))
            Pins.append(Pns.pop(tempsmallestIndex))
            Crosshairs.append(Cross.pop(tempsmallestIndex))
            XCords.append(XCs.pop(tempsmallestIndex))
            YCords.append(YCs.pop(tempsmallestIndex))
        ListofSketches = []
        smallestY = float(Crosshairs[0][1])/10.0
        i = 0
        for i in range(0, len(CompNames)):#For each component in the list of component names...
            #print("i is: "+str(i)+" and number of comps is: "+str(len(CompNames)))
            #print("# of rows in XCords is: "+str(len(XCords))+ ", and it should be: "+str(len(CompNames)))
            CrosshairDiffX = DiffofTwoNums(float(Crosshairs[i][0])/10.0, smallestX)
            #CrosshairDiffX = CrosshairDiffX/2.0
            
            CrosshairDiffY = DiffofTwoNums(float(Crosshairs[i][1])/10.0, smallestY)
            #CrosshairDiffY = CrosshairDiffY/2.0
            
            newComp = adsk.fusion.Component.cast(design.rootComponent)
            extrudes = newComp.features.extrudeFeatures
            sketches = newComp.sketches
            sketch = sketches.add(newComp.xZConstructionPlane)
            sketch.name = str(fileName)+" - "+CompNames[i]

            lines = sketch.sketchCurves.sketchLines
            for c in range(0, len(XCords[i])-1, 2):#For each x-coordinate, y-coordinate and z-coordinate of the current component...
                temp = Crosshairs[i][2]
                result = ''.join(c for c in temp if c.isdigit())
                #print("result is: ."+str(result)+".")
                rotation = int(result)
                #print("rotation is: "+str(rotation))
                r = rotation/90
                for s in range(0, int(r)):
                    newX = -(float(YCords[i][c]))
                    newY = float(XCords[i][c])
                    XCords[i][c] = newX
                    YCords[i][c] = newY
                    newX2 = -(float(YCords[i][c+1]))
                    newY2 = float(XCords[i][c+1])
                    XCords[i][c+1] = newX2
                    YCords[i][c+1] = newY2
                
                startX = x+.2 #2 milimeters from the edge
                startY = y
                
                X1 = float(Crosshairs[i][0])/10.0 + float(XCords[i][c])/10.0
                X1 = X1 - smallestX
                #X1 = X1/2.0
                X2 = float(Crosshairs[i][0])/10.0 + float(XCords[i][c+1])/10.0
                X2 = X2 - smallestX
                #X2 = X2/2.0
                Y1 = float(Crosshairs[i][1])/10.0 + float(YCords[i][c])/10.0
                Y1 = Y1 - smallestY
                #Y1 = Y1/2.0
                Y2 = float(Crosshairs[i][1])/10.0 + float(YCords[i][c+1])/10.0
                Y2 = Y2 - smallestY
                #Y2 = Y2/2.0
                
                startPoint = adsk.core.Point3D.create(startX+X1, startY+Y1, z)
                endPoint = adsk.core.Point3D.create(startX+X2, startY+Y2, z)
                lines.addByTwoPoints(startPoint, endPoint)
            for p in range(0, len(Pins[i])):
                CurrentPin = Pins[i][p]
                
                temp1 = CurrentPin[4]
                temp2 = Crosshairs[i][2]
                result1 = ''.join(c for c in temp1 if c.isdigit())
                #print("result is: ."+str(result1)+".")
                pinRotation = int(result1)
                result2 = ''.join(c for c in temp2 if c.isdigit())
                #print("result is: ."+str(result2)+".")
                CompRotation = int(result2)
                pinLength = float(CurrentPin[3])/10.0
                r = CompRotation/90
                for s in range(0, int(r)):
                    newX = -(float(CurrentPin[2]))
                    newY = float(CurrentPin[1])
                    CurrentPin[1] = newX
                    CurrentPin[2] = newY
                    pinRotation = (pinRotation+90)%360
                pinX = float(CurrentPin[1])/10.0
                pinY = float(CurrentPin[2])/10.0
                    
                
                if(pinRotation == 0):#Pin points LEFT
                    tempX = float(Crosshairs[i][0])/10.0 + pinX
                    X1 = float(Crosshairs[i][0])/10.0 + pinX - pinExtension
                    X2 = tempX + pinLength
                    X1 = X1 - smallestX
                    X2 = X2 - smallestX
                    
                    Y1 = float(Crosshairs[i][1])/10.0 + pinY
                    Y1 = Y1 - smallestY
                    Y2 = Y1
                    
                elif(pinRotation == 90):#Pin points UP
                    X1 = float(Crosshairs[i][0])/10.0 + pinX
                    X1 = X1 - smallestX
                    X2 = X1
                    
                    tempY = float(Crosshairs[i][1])/10.0 + pinY
                    Y1 = float(Crosshairs[i][1])/10.0 + pinY - pinExtension
                    Y2 = tempY + pinLength
                    Y1 = Y1 - smallestY
                    Y2 = Y2 - smallestY
                    
                elif(pinRotation == 180):#Pin points RIGHT
                    tempX = float(Crosshairs[i][0])/10.0 + pinX
                    X1 = float(Crosshairs[i][0])/10.0 + pinX + pinExtension
                    X2 = tempX - pinLength
                    X1 = X1 - smallestX
                    X2 = X2 - smallestX
                    
                    Y1 = float(Crosshairs[i][1])/10.0 + pinY
                    Y1 = Y1 - smallestY
                    Y2 = Y1
                    
                elif(pinRotation == 270):#Pin points DOWN
                    X1 = float(Crosshairs[i][0])/10.0 + pinX
                    X1 = X1 - smallestX
                    X2 = X1
                    
                    tempY = float(Crosshairs[i][1])/10.0 + pinY
                    Y1 = float(Crosshairs[i][1])/10.0 + pinY + pinExtension
                    Y2 = tempY - pinLength
                    Y1 = Y1 - smallestY
                    Y2 = Y2 - smallestY
                
                startX = x+.2 #2 milimeters from the edge
                startY = y
                CurrentPin[0] = " " + CurrentPin[0] + " "
                
                CurrentNet = "Net: "
                for n in range(0, len(Nets)):
                    #print("Nets["+str(n)+"] is: "+str(Nets[n]))
                    for m in range(0, len(Nets[n])):
                        currentNetPin = Nets[n][m]
                        NetsName = currentNetPin[0]
                        NetPinName = " " + currentNetPin[1] + " "
                        NetCompName = currentNetPin[2]
                        if(NetPinName in str(CurrentPin[0]) and NetCompName in str(CompNames[i])):
                            CurrentNet = CurrentNet + NetsName
                
                Pinsketch = sketches.add(newComp.xZConstructionPlane)
                Pinsketch.name = str(fileName)+" - "+CompNames[i]+" - pin:"+ CurrentPin[0] +" "+ CurrentNet
                Pinlines = Pinsketch.sketchCurves.sketchLines

                startPoint = adsk.core.Point3D.create(startX+X1, startY+Y1, z)
                endPoint = adsk.core.Point3D.create(startX+X2, startY+Y2, z)
                Pinlines.addByTwoPoints(startPoint, endPoint)

            ListofSketches.append(sketch)
            
    except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
                