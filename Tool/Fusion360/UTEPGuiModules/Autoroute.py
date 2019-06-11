# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:56:28 2017
@author: jmper

Design Constraints:
1. Model must be in +x, -z, +y quadrant.
2. Contruction plane must be defined by offsetting from xz plane.
"""

import adsk.core, adsk.fusion, adsk.cam, traceback
import math
import os
import inspect
import time
from .Fusion360Router import Router
from .Fusion360Router import MapPrinter
from . import MapFiller

symbol = "-"

def run(context, Ns, CP):
    ui = None
    try:
        #for t in range(0, 5):
        start_time0 = time.time()
        start_time1 = time.time()
        global app
        app = adsk.core.Application.get()
        global ui
        ui = app.userInterface
        global contextt
        contextt = context
        global ConstructionPlane
        ConstructionPlane = CP
        global Nets
        Nets = Ns
        global product
        global design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        Amap, Components, Pins, farleft, fartop, z1 = CreateBoard()
        MapTime = time.time() - start_time1
        #farleft = round(farleft)
        #fartop = round(fartop)
        model = design.activeComponent
        sketches = model.sketches
        newComp = adsk.fusion.Component.cast(model)
        
        start_time2 = time.time()
        tracers, unroutablePairs = Router.initiate_route(Amap, Pins, Components)
        
        flip = tracers[:]
        j=0
        i=len(tracers)-1
        while i >= 0:#flipping map horizontally
            flip[j] = tracers[i]
            j+=1
            i-=1
        newComp = adsk.fusion.Component.cast(design.rootComponent)
        sketch = sketches.add(newComp.xZConstructionPlane)
        sketch.name = "Tracers"
        for i in range(0, len(flip)):
            lines = sketch.sketchCurves.sketchLines
            currentTrace = flip[i] #A TRACE CONSISTS OF SEVERAL TUPLES CORRESPONDING TO COORDINATE POINTS
            for k in range(0, len(currentTrace)-1):
                coordinate1 = currentTrace[k] #COORDINATE1 IS A TUPLE
                x1 = coordinate1[0]
                y1 = coordinate1[1]
                coordinate2 = currentTrace[k+1] #COORDINATE2 IS A TUPLE
                x2 = coordinate2[0]
                y2 = coordinate2[1]
                xdiff1 = x1 + farleft
                ydiff1 = fartop - y1
                xdiff2 = x2 + farleft
                ydiff2 = fartop - y2
                xdiff1 = xdiff1/10.0
                ydiff1 = ydiff1/10.0
                xdiff2 = xdiff2/10.0
                ydiff2 = ydiff2/10.0
                
                Point1 = adsk.core.Point3D.create(xdiff1, ydiff1, z1)
                Point2 = adsk.core.Point3D.create(xdiff2, ydiff2, z1)
                lines.addByTwoPoints(Point1, Point2)
        RoutingTime = time.time() - start_time2
        TotalTime = time.time() - start_time0
        #print("Map["+str(t)+"] created in:---%s seconds ---" % (MapTime))
        #print("Autorouting["+str(t)+"] finished in:---%s seconds ---" % (RoutingTime))
        #print("Completed["+str(t)+"] in:---%s seconds ---" % (TotalTime))
    
        if (unroutablePairs):
            message = ''
            for pair in unroutablePairs:
                message += 'Pair ' + pair.pin.name + ' on '+ pair.pin.component + ' to ' + pair.terminal.name + ' on ' + pair.terminal.component + '\n'
            message2 = "\n\nDo you wish to route these components on another layer?\nIf you select No, please rearrange the components and try again."
            response = ui.messageBox("Not all pairs are routable:\n" + message+message2, "Error Message", 3)
            if(response == 2):#user selected Yes button
                print("blah")
        
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
            
def definePointsOnSketchLine(current_sketch, sketch_evaluator):
    edge_points =[]
    #startPoint and endPoint of subsketch.
    returnValue, startPoint, endPoint = sketch_evaluator.getEndPoints()
    edge_points.append(startPoint)
    #start parameter
    returnValue, start_prm = sketch_evaluator.getParameterAtPoint(startPoint)
    returnValue, end_prm = sketch_evaluator.getParameterAtPoint(endPoint)
    
    #getting length of the sketch and converting into mm
    sketchLength = int(current_sketch.length*10)
    for i in range(1, sketchLength):
        #'i'mm Parameter
        returnValue, leng_imm_prm = sketch_evaluator.getParameterAtLength(start_prm, i/10.0)
        if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
            continue
        
        #imm point
        returnValue, pnt3d = sketch_evaluator.getPointAtParameter(leng_imm_prm)
        
        edge_points.append(pnt3d)
    edge_points.append(endPoint)
    return edge_points

def CreateBoard():
    model = design.activeComponent
    root = design.rootComponent
    sketches = model.sketches
    features = model.features
    bodies = model.bRepBodies
    body = bodies.item(0)
    
    plane = ConstructionPlane 
    sketch2 = sketches.add(plane)
    intersect_sketches = []
    IntersectionSketches = sketch2.intersectWithSketchPlane([body])

    #################################################################################    
    # Loop through subsketches that make up the intersection sketch for drawing.
    
    sketch_names = ""
    for s in range(0, len(IntersectionSketches)):
        currentSketch = IntersectionSketches[s]
        sketch_names += (str(currentSketch.objectType) + "\n")
        
        # An evaluator is determined for each. (Only different if FixedSpline type)
        if(currentSketch.objectType == "adsk::fusion::SketchFixedSpline"):
            eva = currentSketch.evaluator
        else:
            eva = currentSketch.geometry.asNurbsCurve.evaluator

        # Method called to add points on subsketch to list edge_points
        intersect_sketches.append(definePointsOnSketchLine(currentSketch, eva))
    ui.messageBox(sketch_names)
    #################################################################################    

    #################################################################################    
    # Create Bounding box for Map array used for routing in RoutingLog.txt
    # by finding least and greatest perimiter points of the model in x and y.
    
    farleft = math.inf
    farright = -math.inf
    farbottom = math.inf
    fartop = -math.inf
    
    # Height of construction plane, y coordinate.
    z1 = plane.geometry.origin.y
    
    # Find least and greatest points in x and y
    for intersect_sketch in intersect_sketches:        
        for edge_point in intersect_sketch:
            x1 = (edge_point.x)
            y1 = (edge_point.y)
    
            if(farleft > x1):
                farleft = x1
            if(farright < x1):
                farright = x1
            
            if(farbottom > y1):
                farbottom = y1
            if(fartop < y1):
                fartop = y1

    '''
    ui.messageBox("fl: " + str(farleft) + "\n"
                +"fr: " + str(farright) + "\n"
                +"fb: " + str(int(farbottom)) + "\n"
                +"ft: " + str(fartop) + "\n"
                +"Y HEIGHT: " + str(z1))
    '''
    # Add 1cm (10 mm/spaces) each direction for cushion then convert to mm.
    farleft = (farleft - 1.0) * 10
    farright = (farright + 1.0) * 10
    farbottom = (farbottom - 1.0) * 10
    fartop = (fartop + 1.0) * 10
    #################################################################################    
                
    #################################################################################    
    # Map Creation by finding difference in coordinates

    xdiff = int(farright - farleft) 
    ydiff = int(fartop - farbottom)
    
    # Double loop to make 2d-list xdiff by ydiff full of empty character 'e'
    Amap = [['e' for i in range(ydiff)] for j in range(xdiff)]
    #################################################################################    

    Amap, Components, Pins = FillMap(Amap, intersect_sketches, farleft, fartop, z1)
    return Amap, Components, Pins, farleft, fartop, z1
    
    

def ConnectLine(Amap, coordinates, letter):
    #CONNECTING THE POINTS OF THE OUTER EDGES OF THE MAP    
    i = 0
    while i < len(coordinates)-1:
        x1 = coordinates[i%len(coordinates)][0]
        y1 = coordinates[i%len(coordinates)][1]
        x2 = coordinates[(i+1)%len(coordinates)][0]
        y2 = coordinates[(i+1)%len(coordinates)][1]
        #IF X'S ARE EQUAL, THERE IS A VERTICAL LINE
        if(int(x1) == int(x2)):
            m = 0;
            b = y1-m*x1
            if( (y2-y1) < 0):
                for j in range(0, (y2-y1), -1):
                    y = y1 + j
                    x = x1
                    Amap[int(x)][int(y)] =str(letter)
            else:
                for j in range(0, (y2-y1)):
                    y = y1 + j
                    x = x1
                    Amap[int(x)][int(y)] =str(letter)
        #ELSE, IT IS EITHER A HORIZONTAL OR DIAGONAL LINE.
        elif(x1 != x2):
            m = float(y2-y1)/float(x2-x1)
            b = y1-m*x1
            #IF THE LINE IS DIAGONAL...
            if(x1 != x2 and y1 != y2):
                #DIAG LINE GOING UP-RIGHT
                if( ((x2-x1) >= 0) and ((y2-y1) >= 0) ):
                    diagxs = []
                    diagys = []
                    for j in range(0, (x2-x1), -1):
                        x = x1 + j
                        y = (m*x)+b
                        Amap[int(x)][int(y)] =str(letter)
                        diagxs.append(x)
                        diagys.append(y)
                        ConnectDiagonal(diagxs, diagys, Amap, letter)
                    ConnectDiagonal(diagxs, diagys, Amap, letter)
                
                #DIAG LINE GOING DOWN-RIGHT
                elif( ((x2-x1) >= 0) and ((y2-y1) < 0) ):
                    diagxs = []
                    diagys = []
                    for j in range(0, (y2-y1)):
                        y = y1 + j
                        x = (m*y)+b
                        #x = x1 + j
                        #y = (m*x)+b
                        Amap[int(x)][int(y)] =str(letter)
                        diagxs.append(x)
                        diagys.append(y)
                        ConnectDiagonal(diagxs, diagys, Amap, letter)
                    ConnectDiagonal(diagxs, diagys, Amap, letter)
                
                #DIAG LINE GOING DOWN-LEFT
                elif( ((x2-x1) < 0) and ((y2-y1) < 0) ):
                    diagxs = []
                    diagys = []
                    for j in range(0, (x2-x1), -1):
                        x = x1 + j
                        y = (m*x)+b
                        Amap[int(x)][int(y)] =str(letter)
                        diagxs.append(x)
                        diagys.append(y)
                        ConnectDiagonal(diagxs, diagys, Amap, letter)
                    ConnectDiagonal(diagxs, diagys, Amap, letter)
                
                #DIAG LINE GOING UP-LEFT
                elif( ((x2-x1) < 0) and ((y2-y1) >= 0) ):
                    diagxs = []
                    diagys = []
                    for j in range(0, (y2-y1), -1):
                        y = y1 + j
                        x = (m*y)+b
                        #x = x1 + j
                        #y = (m*x)+b
                        Amap[int(x)][int(y)] =str(letter)
                        diagxs.append(x)
                        diagys.append(y)
                        ConnectDiagonal(diagxs, diagys, Amap, letter)
                    ConnectDiagonal(diagxs, diagys, Amap, letter)
            
            #IF THE LINE IS HORIZONTAL
            elif(x1 != x2 and y1 == y2):
                if( (x2-x1) < 0):
                    for j in range(0, (x2-x1), -1):
                        x = x1 + j
                        y = (m*x)+b
                        Amap[int(x)][int(y)] =str(letter)
                else:
                    for j in range(0, (x2-x1)):
                        x = x1 + j
                        y = (m*x)+b
                        Amap[int(x)][int(y)] =str(letter)
            if( (x2-x1) < 0):
                for j in range(0, (x2-x1), -1):
                    x = x1 + j
                    y = (m*x)+b
                    Amap[int(x)][int(y)] =str(letter)
            else:
                for j in range(0, (x2-x1)):
                    x = x1 + j
                    y = (m*x)+b
                    Amap[int(x)][int(y)] =str(letter)
        i+=1
    



def ConnectDiagonal(diagxs, diagys, Amap, letter):
    for i in range(0, len(diagxs)-1):
        x1 = diagxs[i]
        x2 = diagxs[i+1]
        y1 = diagys[i]
        y2 = diagys[i+1]
        m = float(y2-y1)/float(x2-x1)
        b = y1-m*x1
        if(x1 != x2 and y1 != y2):
            #DIAG LINE GOING UP-RIGHT
            if( ((x2-x1) >= 0) and ((y2-y1) >= 0) ):
                for j in range(0, (x2-x1), -1):
                    x = x1 + j
                    y = (m*x)+b
                    Amap[int(x)][int(y)] =str(letter)
            
            #DIAG LINE GOING DOWN-RIGHT
            elif( ((x2-x1) >= 0) and ((y2-y1) < 0) ):
                for j in range(0, (y2-y1)):
                    y = y1 + j
                    x = (m*y)+b
                    #x = x1 + j
                    #y = (m*x)+b
                    Amap[int(x)][int(y)] =str(letter)
            
            #DIAG LINE GOING DOWN-LEFT
            elif( ((x2-x1) < 0) and ((y2-y1) < 0) ):
                for j in range(0, (x2-x1), -1):
                    x = x1 + j
                    y = (m*x)+b
                    Amap[int(x)][int(y)] =str(letter)
            
            #DIAG LINE GOING UP-LEFT
            elif( ((x2-x1) < 0) and ((y2-y1) >= 0) ):
                for j in range(0, (y2-y1), -1):
                    y = y1 + j
                    x = (m*y)+b
                    #x = x1 + j
                    #y = (m*x)+b
                    Amap[int(x)][int(y)] =str(letter)





def EdgeToMap(edges, Amap, coordinates, symbol, x, y):
    for e in range(0, len(edges)):
        edge = edges.item(e).geometry
        #ui.messageBox("edge objectType is: "+str(edge.objectType))
        if(edge.objectType == "adsk::core::Arc3D"):
            ArcPoints = []
            eva = edge.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(edge.length*10)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            
        elif(edge.objectType == "adsk::core::Circle3D"):
            ArcPoints = []
            eva = edge.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(edge.length*10)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
        elif(edge.objectType == "adsk::core::Ellipse3D"):
            ArcPoints = []
            eva = edge.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(edge.length*10)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
        elif(edge.objectType == "adsk::core::EllipticalArc3D"):
            ArcPoints = []
            eva = edge.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(edge.length*10)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
        elif(edge.objectType == "adsk::core::InfiniteLine3D"):
            print("blah")
        elif(edge.objectType == "adsk::core::Line3D"):
            ArcPoints = edge.asNurbsCurve.controlPoints
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.z*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                #print("startX = "+str(startX)+", startY = "+str(startY))
                #print("x = "+str(x)+", y = "+str(y))
                #print("xdiff = "+str(xdiff)+", ydiff = "+str(ydiff))
                #print("len(Amap) = "+str(len(Amap))+", len(Amap[0]) = "+str(len(Amap[0])))
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.z*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
        elif(edge.objectType == "adsk::core::NurbsCurve3D"):
            ArcPoints = []
            eva = edge.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(edge.length*10)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
    return Amap, coordinates





def SketchToMap(Sketches, Amap, x, y):
    for s in range(0, len(Sketches)):
        currentSketch = Sketches[s]
        if(currentSketch.objectType == "adsk::fusion::SketchArc"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
                
        elif(currentSketch.objectType == "adsk::fusion::SketchCircle"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
        
        elif(currentSketch.objectType == "adsk::fusion::SketchConicCurve"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
        
        elif(currentSketch.objectType == "adsk::fusion::SketchEllipse"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
        
        elif(currentSketch.objectType == "adsk::fusion::SketchEllipticalArc"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
        
        elif(currentSketch.objectType == "adsk::fusion::SketchFittedSpline"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
        
        elif(currentSketch.objectType == "adsk::fusion::SketchFixedSpline"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
            
        elif(currentSketch.objectType == "adsk::fusion::SketchLine"):
            ArcPoints = []
            coordinates = []
            eva = currentSketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(currentSketch.length*100)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i/100.0)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = symbol
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = symbol
            ConnectLine(Amap, coordinates, symbol)
        
    return Amap


def FillHole(Amap, coordinates):
    #FILLING THE MAP WITH THE HOLES
    farleft = math.inf
    farright = -math.inf
    farbottom = math.inf
    fartop = -math.inf
    for c in range(0, len(coordinates)):
        x1 = coordinates[c][0]
        y1 = coordinates[c][1]
        if(farleft > x1):
            farleft = x1
        if(farright < x1):
            farright = x1
        if(farbottom > y1):
            farbottom = y1
        if(fartop < y1):
            fartop = y1
    farleft = farleft - 1
    farright = farright + 1
    farbottom = farbottom - 1
    fartop = fartop + 1
    slicedMap = [Amap[i][farbottom:fartop] for i in range(farleft,farright)]
    #slicedMap = Amap[farleft:farright, farbottom:fartop]
    rotated = list(zip(*slicedMap[::-1]))
    for i in range(0, len(rotated)):
        rotated[i] = list(rotated[i])
    for f in range(0, len(rotated)):
        temp = (rotated[f])
        if '-' in temp:
            firstM = temp.index('-')
            lastM = len(temp) - 1 - temp[::-1].index('-')
            temp2 = (temp[firstM:lastM])
            if 'e' in temp2:
                firstE = temp2.index('e')
                firstE = firstE +firstM + 1
                lastE = len(temp2) - 1 - temp2[::-1].index('e')
                lastE = lastE + firstM + 1
                for k in range(firstE, lastE):
                    rotated[f][k] = 'e'
    rotated = list(zip(*rotated[::-1]))
    rotated = list(zip(*rotated[::-1]))
    
    
    
    
    slicedMap = list(zip(*rotated[::-1]))
    for i in range(0, len(slicedMap)):
        slicedMap[i] = list(slicedMap[i])
        
    for f in range(0, len(slicedMap)):
        temp = (slicedMap[f])
        if '-' in temp:
            firstM = temp.index('-')
            lastM = len(temp) - 1 - temp[::-1].index('-')
            temp2 = (temp[firstM:lastM])
            if 'e' in temp2:
                firstE = temp2.index('e')
                firstE = firstE +firstM + 1
                lastE = len(temp2) - 1 - temp2[::-1].index('e')
                lastE = lastE + firstM + 1
                for k in range(firstE, lastE):
                    slicedMap[f][k] = 'e'
    for i in range(farleft, farright):
        for j in range(farbottom, fartop):
            Amap[i][j] = slicedMap[i%farleft][j%farbottom]
    return Amap


def FillMap(Amap, intersect_sketches, x, y, z):
    
    global model
    model = design.activeComponent

    # Get model features
    features = model.features
    holes = features.holeFeatures
    extrusions = features.extrudeFeatures
    
    # Get sketches to make intersection sketch.
    sketches = model.sketches
    plane = ConstructionPlane
    body = model.bRepBodies.item(0)

    sketch2 = sketches.add(plane)
    Components = []
    Pins = []
    #ADDING THE PERIMETER OF THE MODEL TO THE MAP
    IntersectionSketches = sketch2.intersectWithSketchPlane([body])
    #symbol = '-'
    #GET THE OUTLINE OF THE MODEL
    Amap = SketchToMap(IntersectionSketches, Amap, x, y)    
    
    #FILLING THE MAP WITH THE BODY
    #######################################################################
    #CArlos MEthod of Filling MAp
    dirName = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    filename = dirName + '\\'+"AutorouteMapPreFill.txt"    
   	
    #Need to make center X and Y automatically within the shape
    # a good point might be the corner of any component since the user will not place it
    # outside of the shape.
    
    #centerX = 100
    #centerY = 100
    
    centerX = 32
    centerY = 32

    Amap[centerX][centerY] = 'X'
    MapPrinter.printMapFile(Amap, filename)
    center = (centerX,centerY) #point filling in begins from
    MapFiller.BubbleFillMap(Amap,center)
    #######################################################################
    
    
    #CHECKING FOR POSSIBLE HOLES/CAVITIES MADE BY THE HOLE FUNCTION    
    coordinates = []    
    if(holes.count > 0):
        for h in range(0, holes.count):
            coordinates = []
            hole = holes.item(h)
            diameter = hole.holeDiameter.value
            radius = diameter/2.0
            center = hole.position
            Circlex = center.x
            Circley = -center.z
            Circlez = center.y
            center2 = adsk.core.Point3D.create(Circlex, Circley, Circlez)
            circles = sketch2.sketchCurves.sketchCircles
            holesketch = circles.addByCenterRadius(center2, radius)
            if(Circlez != z):
                continue
            ArcPoints = []
            eva = holesketch.geometry.asNurbsCurve.evaluator
            #startPoint&endPoint
            returnValue, startPoint, endPoint = eva.getEndPoints()
            
            #start parameter
            returnValue, start_prm = eva.getParameterAtPoint(startPoint)
            returnValue, end_prm = eva.getParameterAtPoint(endPoint)
            ArcPoints.append(startPoint)
            
            #getting length of the sketch and converting into mm
            sketchLength = int(holesketch.length*10)
            for i in range(1, sketchLength):
                #'i'mm Parameter
                returnValue, leng_imm_prm = eva.getParameterAtLength(start_prm, i)
                if( not((start_prm < leng_imm_prm) and (leng_imm_prm < end_prm))):
                    continue
                #imm point
                returnValue, pnt3d = eva.getPointAtParameter(leng_imm_prm)
                
                ArcPoints.append(pnt3d)
            ArcPoints.append(endPoint)
            for a in range(0, len(ArcPoints)-1):
                startPoint = ArcPoints[a]
                endPoint = ArcPoints[a+1]
                startX = abs(startPoint.x*10)
                startY = abs(startPoint.y*10)
                xdiff = int(round(abs(x-startX)))
                ydiff = int(round(abs(y-startY)))
                xdiff -= 1
                ydiff -= 1
                if(xdiff<0):
                    continue
                if(ydiff<0):
                    continue
                if(xdiff>=len(Amap)):
                    continue
                if(ydiff>=len(Amap[0])):
                    continue
                temp = []
                temp.append(xdiff)
                temp.append(ydiff)
                coordinates.append(temp)
                Amap[xdiff][ydiff] = 'e'
                
                endX = abs(endPoint.x*10)
                endY = abs(endPoint.y*10)
                xdiff2 = int(round(abs(x-endX)))
                ydiff2 = int(round(abs(y-endY)))
                xdiff2 -= 1
                ydiff2 -= 1
                if(xdiff2<0):
                    continue
                if(ydiff2<0):
                    continue
                temp = []
                temp.append(xdiff2)
                temp.append(ydiff2)
                coordinates.append(temp)
                Amap[xdiff2][ydiff2] = 'e'
                #CONNECTING THE POINTS OF THE LINE SEGMENT
                ConnectLine(Amap, coordinates, 'e')
                Amap = FillHole(Amap, coordinates)
            ConnectLine(Amap, coordinates, 'e')
    
    #CHECKING FOR POSSIBLE HOLES/CAVITIES MADE BY THE EXTRUDE FUNCTION
    PossibleHoles = [] 
    for e in range(0, extrusions.count):
        currentExtrusion = extrusions.item(e)            
        if(currentExtrusion.operation == 1):#The feature cuts or removes materials.
            PossibleHoles.append(currentExtrusion)
    #ui.messageBox("Number of possible holes is: "+str(len(PossibleHoles)))
    for p in range(0, len(PossibleHoles)):
        currentHole = PossibleHoles[p]
        #print("In hole #: "+str(p))
        faces = currentHole.faces
        for f in range(0, faces.count):
            face = faces.item(f)
            #print("face["+str(f)+"] is: "+str(face.centroid.x)+", "+str(face.centroid.y)+", "+str(-face.centroid.z))
            #print("z is: "+str(z))
            Point1 = adsk.core.Point3D.create(face.centroid.x, -face.centroid.z, z*10)
            sketches = model.sketches
            newComp = adsk.fusion.Component.cast(design.rootComponent)
            #sketches = newComp.sketches
            sketch = sketches.add(newComp.xZConstructionPlane)
            modelPoint = sketch.sketchToModelSpace(Point1)
            #ui.messageBox("pointContainment is: "+str(body.pointContainment(modelPoint)))
            if(body.pointContainment(modelPoint) == 2):
                edges = face.edges
                coordinates = []
                symbol = 'e'
                Amap, coordinates = EdgeToMap(edges, Amap, coordinates, symbol, x, y)
                ConnectLine(Amap, coordinates, symbol)
                #Amap = FillHole(Amap, coordinates)
            
           

    ui.messageBox(str(sketches.count)) #####################3 DEBUG

    #ADDING THE PERIMETER OF THE COMPONENTS TO THE MAP
    for s in range(0, sketches.count):
        
#        if(sketches.item(s).sketchPoints.item(0).geometry.z != z):
#            print("Sketch Point z is: "+str(sketches.item(s).sketchPoints.item(0).geometry.z))
#            print("z is: "+str(z))
#            continue
        if(".sch" in str(sketches.item(s).name)):
            if("- pin:" in str(sketches.item(s).name)):
                sketchcoordinates = []
                currentPin = []
                sketchName = sketches.item(s).name
                index = sketchName.index("- pin:")
                index2 = sketchName.index("Net:")
                index3 = sketchName.index(".sch - ")
                pinname = sketchName[index+7:index2-2]
                componentname = sketchName[index3+7:index]
                #print("Current Component is: "+str(componentname)+ ", and pin is: "+str(pinname))
                netname = sketchName[index2+5:]
                if(netname.isspace() or netname == ''):
                    netname = '-'
                PinPosition = ()
                p = 1
                broke = 0
                ui.messageBox(str(sketches.item(s).sketchPoints.count)) ################################## DEBUG
                while(p < sketches.item(s).sketchPoints.count): 
                    pinX = abs(sketches.item(s).sketchPoints.item(p).geometry.x*10)
                    pinY = abs(sketches.item(s).sketchPoints.item(p).geometry.y*10)
                    pinZ = abs(sketches.item(s).sketchPoints.item(p).geometry.z*10)
                    if(math.isclose(pinZ, z*10, rel_tol=0.05, abs_tol=0.0) == False):
                        print("pinX is: "+str(pinX)+"\npinY is: "+str(pinY)+"\npinZ is: "+str(pinZ))
                        print("z is: "+str(z))
                        broke = 1
                        break
                    sketches.item(s).isVisible = True
                    xdiff = int(round(abs(x-pinX)))
                    ydiff = int(round(abs(y-pinY)))

                    CurrentNet = ""
                    for n in range(0, len(Nets)):
                        for m in range(0, len(Nets[n])):
                            currentNetPin = Nets[n][m]
                            NetsName = currentNetPin[0]
                            NetPinName = currentNetPin[1]
                            NetCompName = currentNetPin[2]
                            if(NetPinName in str(sketches.item(s).name) and NetCompName in str(sketches.item(s).name)):
                                CurrentNet = NetsName
                    if(xdiff<0):
                        continue
                    if(ydiff<0):
                        continue
                    if(xdiff >= len(Amap) or ydiff >= len(Amap[0])):
                        break
                    temp = []
                    temp.append(xdiff)
                    temp.append(ydiff)
                    sketchcoordinates.append(temp)
                    p = p + 1
                    ConnectLine(Amap, sketchcoordinates, 'o')
                    lastx = sketchcoordinates[0][0]
                    lasty = sketchcoordinates[0][1]
                    Amap[lastx][lasty] = netname
                if(broke == 0):
                    PinPosition = PinPosition + (lastx, )
                    PinPosition = PinPosition + (lasty, )
                    currentPin.append(pinname)
                    currentPin.append(netname)
                    currentPin.append(PinPosition)
                    currentPin.append(componentname)
                    Pins.append(currentPin)
                    
#ADDING COMPONENTS TO THE MAP        
            else:
                sketchcoordinates = []
                currentComponent = []
                sketchName = sketches.item(s).name
                print("Current Component is: "+str(sketchName))
                index = sketchName.index(".sch")
                Compname = sketchName[index+7:]
                CompPosition = []
                p = 1
                broke = 0
                while(p < sketches.item(s).sketchPoints.count):
                    sketchX = abs(sketches.item(s).sketchPoints.item(p).geometry.x*10)
                    sketchY = abs(sketches.item(s).sketchPoints.item(p).geometry.y*10)
                    sketchZ = abs(sketches.item(s).sketchPoints.item(p).geometry.z*10)
                    if(math.isclose(sketchZ, z*10, rel_tol=0.05, abs_tol=0.0) == False):
                        print("sketchX is: "+str(sketchX)+"\nsketchY is: "+str(sketchY)+"\nsketchZ is: "+str(sketchZ))
                        print("z is: "+str(z))
                        broke = 1
                        break
                    sketches.item(s).isVisible = True
                    xdiff = int(round(abs(x-sketchX)))
                    ydiff = int(round(abs(y-sketchY)))
                    
                    if(xdiff<0):
                        continue
                    if(ydiff<0):
                        continue
                    if(xdiff >= len(Amap) or ydiff >= len(Amap[0])):
                        break
                    temp = []
                    temp.append(xdiff)
                    temp.append(ydiff)
                    sketchcoordinates.append(temp)
                    Amap[xdiff][ydiff] = 'o'
                    currentPosition = ()
                    currentPosition = currentPosition + (xdiff, )
                    currentPosition = currentPosition + (ydiff, )
                    CompPosition.append(currentPosition)
                    ConnectLine(Amap, sketchcoordinates, 'o')
                    p = p + 1
                if(broke == 0):
                    currentComponent.append(Compname)
                    currentComponent.append(CompPosition)
                    Components.append(currentComponent)
                
 
    dirName = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    filename = dirName + '\\'+"AutorouteMap.txt"
    with open(filename, 'w') as file_handler:
        '''
        for item in Amap:
            file_handler.write("{}\n".format(item))
        '''
        for x in range(len(Amap[0])):
            for y in range(len(Amap)):
                if len(Amap[y][x]) == 1:
                    space = '   '
                elif len(Amap[y][x]) == 0:
                    space = '    '
                elif len(Amap[y][x]) == 2:
                    space = '  '
                elif len(Amap[y][x]) == 3:
                    space = ' '
                else:
                    space = ''
                file_handler.write(space + Amap[y][x])
            file_handler.write("\n")
            
    return Amap, Components, Pins
