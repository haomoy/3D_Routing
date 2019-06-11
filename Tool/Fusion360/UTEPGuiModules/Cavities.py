# -*- coding: utf-8 -*-
"""
Created on Wed May 30 10:25:07 2018

@author: jmperez6
"""
import adsk.core, adsk.fusion, adsk.cam, traceback
import math
def MakeCavities(Heights):
    app = adsk.core.Application.get()
    ui = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    model = design.activeComponent
    sketches = model.sketches
    #newComp = adsk.fusion.Component.cast(design.rootComponent)
    extrudes = model.features.extrudeFeatures
    j = 0
    #EXTRUDING THE SKETCHES    
    for k in range(0, len(sketches)):
        if(".sch" in str(sketches.item(k).name) and "- pin:" not in str(sketches.item(k).name)):
            currentSketch = sketches.item(k)
            CompandPins = []
            for m in range(k, len(sketches)):
                if(currentSketch.name in sketches.item(m).name and "- pin:" in str(sketches.item(m).name)):
                    CompandPins.append(sketches.item(m))
            CompandPins.append(currentSketch)
            farleft = math.inf
            farright = -math.inf#largest y that is paired with the largest x or smallestx.
            farbottom = math.inf
            fartop = -math.inf
           
            for v in range(0, len(CompandPins)):
                Lines = CompandPins[v].sketchCurves.sketchLines
                for a in range(0, Lines.count):
                    LinePoints = Lines.item(a).geometry.asNurbsCurve.controlPoints
                    for b in range(0, len(LinePoints)):
                        vertex = LinePoints[b]
                        x1 = vertex.x
                        y1 = vertex.y
                        if(farleft > x1):
                            farleft = x1 - .1
                        if(farright < x1):
                            farright = x1 + .1
                        if(farbottom > y1):
                            farbottom = y1 - .1
                        if(fartop < y1):
                            fartop = y1 + .1
            z1 = currentSketch.sketchPoints.item(1).geometry.z
            newComp = adsk.fusion.Component.cast(design.rootComponent)
            sketch = sketches.add(newComp.xZConstructionPlane)
            lines = sketch.sketchCurves.sketchLines
            lines.addByTwoPoints((adsk.core.Point3D.create(farright, fartop, z1)), (adsk.core.Point3D.create(farright, farbottom, z1)))
            lines.addByTwoPoints((adsk.core.Point3D.create(farright, farbottom, z1)), (adsk.core.Point3D.create(farleft, farbottom, z1)))
            lines.addByTwoPoints((adsk.core.Point3D.create(farleft, farbottom, z1)), (adsk.core.Point3D.create(farleft, fartop, z1)))
            lines.addByTwoPoints((adsk.core.Point3D.create(farleft, fartop, z1)), (adsk.core.Point3D.create(farright, fartop, z1)))
            
            # Get the extrusion body
            profRec = sketch.profiles.item(0)
            # Define that the extent is a distance extent of 'n' cm
            n = Heights[j]
            height = float(-.01)#default height, 1mm
            if("NA" not in str(n)):
                height = -float(n)/10.0
            distance = adsk.core.ValueInput.createByReal(height)
            extrudeCut = extrudes.addSimple(profRec, distance, adsk.fusion.FeatureOperations.CutFeatureOperation)
            extrudeCut.name = sketches.item(k).name+" - Extrusion"
            # Set the extrude to be a solid one
            extrudeCut.isSolid = True
            # Get the state of the extrusion
            health = extrudeCut.healthState
            if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
                ui.messageBox("Complications on timelineObj", "Error Window")        
                # Get the state of timeline object
                timeline = design.timeline
                timelineObj = timeline.item(timeline.count - 1);
                health = timelineObj.healthState
                if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:       
                    ui.messageBox("Complications on timelineObj", "Error Window")
            j = j + 1