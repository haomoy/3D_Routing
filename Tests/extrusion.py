import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Get sketch texts 
        sketchTexts = sketch.sketchTexts        
        # Create sketch text input
        point = adsk.core.Point3D.create(1.0, 1.0, 1.0)
        sketchTextInput = sketchTexts.createInput('example', 1.0, point)
        # Create sketch text
        sketchText = sketchTexts.add(sketchTextInput)
         
        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(sketchText, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(0.1)
        extInput.setDistanceExtent(False, distance)
        extInput.isSolid = True
        
        # Create the extrusion
        ext = extrudes.add(extInput)

           
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))