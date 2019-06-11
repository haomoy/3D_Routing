#Author-Jazmin Munoz & Jose M. Perez Jr.
import adsk.core, adsk.fusion, traceback
import ctypes 


def CreateReference2():
    app = adsk.core.Application.get()
    ui = app.userInterface
    ##ui.messageBox("Inside Create Reference 2!!!")
    global temp
    global lastx
    global lasty
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)
    newComp = adsk.fusion.Component.cast(design.rootComponent)
    # Create an extrusion input
    sketches = newComp.sketches 
    sketch = sketches.add(newComp.xZConstructionPlane)
    ##print("---------------------------------------------------------------------------")
#    sketchCircles = sketch.sketchCurves.sketchCircles
#    centerPoint = adsk.core.Point3D.create(0, 0, 0)
#    sketchCircles.addByCenterRadius(centerPoint, 3.0)
    sketchLines = sketch.sketchCurves.sketchLines
    
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(9, 9, 0), adsk.core.Point3D.create(9, 4, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(9, 4, 0), adsk.core.Point3D.create(12, 4, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(12, 4, 0), adsk.core.Point3D.create(12, 6, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(12, 6, 0), adsk.core.Point3D.create(10, 6, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(10, 6, 0), adsk.core.Point3D.create(10, 8, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(10, 8, 0), adsk.core.Point3D.create(12, 8, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(12, 8, 0), adsk.core.Point3D.create(12, 9, 0))
    sketchLines.addByTwoPoints(adsk.core.Point3D.create(12, 9, 0), adsk.core.Point3D.create(9, 9, 0))
#    
    
    #sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(4, 4, 0), adsk.core.Point3D.create(-4, -4, 0))
    
    # Get the profile defined by the circle
    prof = sketch.profiles.item(0)
    
    # Create an extrusion input
    extrudes = newComp.features.extrudeFeatures
    extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    
    # Define that the extent is a distance extent of 5 cm
    distance = adsk.core.ValueInput.createByReal(1)
    # Set the distance extent to be symmetric
    extInput.setDistanceExtent(True, distance)
    # Set the extrude to be a solid one
    extInput.isSolid = True
    
    # Create the extrusion
    ext = extrudes.add(extInput)
    
    # Get the body created by the extrusion
    body = ext.bodies.item(0)
    
    axes = newComp.constructionAxes
    axisInput = axes.createInput()
    # Add by line
    if design.designType == adsk.fusion.DesignTypes.DirectDesignType:
        axisInput.setByLine(adsk.core.InfiniteLine3D.create(adsk.core.Point3D.create(0), adsk.core.Vector3D.create(1, 0, 0)))
        axes.add(axisInput)
        
        # Prepare reference data
        circularFace = None
        for face in body.faces:
            geom = face.geometry
            if geom.surfaceType == adsk.core.SurfaceTypes.CylinderSurfaceType:
                circularFace = face
                break
            
            linearEdge = None
            for edge in body.edges:
                edgeGeom = edge.geometry
                if edgeGeom.curveType == adsk.core.Curve3DTypes.Line3DCurveType:
                    linearEdge = edge
                    break
                
            faceOne = linearEdge.faces.item(0)
            faceTwo = linearEdge.faces.item(1)
            vertexOne = faceOne.vertices.item(0)
            vertexTwo = faceOne.vertices.item(1)
            
            # Add by circularFace
            axisInput.setByCircularFace(circularFace)
            axes.add(axisInput)
            
            # Add by perpendicular at point
            axisInput.setByPerpendicularAtPoint(faceOne, vertexOne)
            axes.add(axisInput)
            
#   Add by o planes
            axisInput.setByTwoPlanes(faceOne, faceTwo)
            axes.add(axisInput)
            
#   Add by o points
            axisInput.setByTwoPoints(vertexOne, vertexTwo)
            axes.add(axisInput)
            
            # Add by edge
            axisInput.setByEdge(linearEdge)
            axes.add(axisInput)
            
            # Add by normal to face at point
            axisInput.setByNormalToFaceAtPoint(faceTwo, vertexOne)
            axis = axes.add(axisInput)
            
            # Get health state of the axis
            health = axis.healthState
            if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
                ctypes.windll.user32.MessageBoxW(0, "OH NO!", "Your title", 1)
                
    #print("---------------------------------------------------------------------------")
    #ui.messageBox('cow')   
