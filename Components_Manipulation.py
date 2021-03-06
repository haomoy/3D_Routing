import adsk.core, adsk.fusion, adsk.cam, traceback
import os
import math
import inspect
from .Sketching import component_sketcher as CS 

#Replace all references to SIE and NIE with CC
from .File_Extraction.xml_information_extraction import component_collector as CC

#from . import Autoroute as CREATEMAP ########## IMPORT ONCE I MAKE MY OWN ROUTING AGENT
#from . import Cavities as CAV ########## IMPORT ONCE I MAKE MY OWN CAVITY FILE

handlers = []
app = None
ui  = None
commandId = 'CommandInputGallery'
commandName = 'Command Input Gallery'
commandDescription = 'Demo command input examples.'
rowNumber = 0

# Global set of event handlers to keep them referenced for the duration of the command
handlers = []


# Event handler for the execute event.
class UTEPMultiProcessButtonPressedCommandInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.InputChangedEventArgs.cast(args)

        # Code to react to the event.
        app = adsk.core.Application.get()
        ui  = app.userInterface
        try:
            cmdInput = eventArgs.input
            inputs = eventArgs.inputs
            global buttonClicked
            buttonClicked = ''
            
            
            if cmdInput.id == '_help2':
                ui.messageBox("Instructions on how to use this tab:\n\n 1. Below this Help button, is the list of the selected files. For each of these items, use the 'Select' tool to select a construction plane.\n 2. Once all 'Select' tools are highlighted, input a value in the Extension box if you want to extend the pins of each component, if not, leave it at its default value. Afterwards click on 'Place' at the very bottom of the list to place all the components of the selected files to their respective construction planes.\n You'll need to close the GUI to move the components around. \n 3. Once you have moved the components to where you want them, click on Autoroute to create the tracers for the components. \n 4. Once there tracers are placed, click on Save Tracers to save the tracers as a DXF file. \n 5. Once the tracers have been saved, click on Create Cavities to create the cavities for each of the components. Once this is done, you can save the model as an STL file by selecting it under the Browser folder, with the lightbulb symbols, right click the body and select 'Save as STL'")
            
            
            elif cmdInput.id == '_place':
                buttonClicked = "_place"
                cmd.doExecute(False)
                buttonClicked = ""
            
            elif cmdInput.id == '_autoroute':
                buttonClicked = "_autoroute"
                cmd.doExecute(False)
                buttonClicked = ""

            elif cmdInput.id == '_cavity':
                buttonClicked = "_cavity"
                cmd.doExecute(False)
                buttonClicked = ""

            elif cmdInput.id == '_DXF':
                buttonClicked = "_DXF"
                cmd.doExecute(False)
                buttonClicked = ""
            # Check to see if it was the selection input changed.
            for n in range(0, len(SelectedFiles)):
                if eventArgs.input.id == '_selection'+str(n):
                    selectionInput = adsk.core.SelectionCommandInput.cast(eventArgs.input)
                    if selectionInput.selectionCount == 1:
                        selectionTable = tab1ChildInputs.itemById('_table'+str(n))
                        selectionTextBox = selectionTable.getInputAtPosition(n, 1)
                        selectionTextBox.numRows = 3
                        selectionTextBox.text = "X: "+str(selectionInput.selection(0).point.x)+",\n Y: "+str(selectionInput.selection(0).point.y)+",\n Z:"+str(selectionInput.selection(0).point.z)
                    else:
                        selectionTable = tab1ChildInputs.itemById('_table'+str(n))
                        selectionTextBox = selectionTable.getInputAtPosition(n, 1)
                        selectionTextBox.numRows = 3
                        selectionTextBox.text = ""

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc())) 

        
class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # When the command is done, terminate the script
            # This will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            app = adsk.core.Application.get()
            ui = app.userInterface
            global cmd
            cmd = args.command
            cmd.isOKButtonVisible = False
            global inputss
            inputss = cmd.commandInputs
            global commandId
            commandId = 'ComponentGallery'
            # Create tab input 1
            tabCmdInput1 = inputss.addTabCommandInput(commandId + '_table_1', 'Component Placement');
            global tab1ChildInputs            
            tab1ChildInputs = tabCmdInput1.children;
            
            
            # Help
           #n tab1ChildInputs.addBoolValueInput('_help2', 'Help', False, '', True)


            # Create input bar that takes double values to specify pin extension
            tab1ChildInputs.addValueInput('_extension', 'Pin Extension', 'mm', adsk.core.ValueInput.createByReal(0.0))
            # Create bool value input with button style to place components
            tab1ChildInputs.addBoolValueInput('_place', 'Place', False, '', True)
            # Create bool value input with button style to autoroute placed components
            tab1ChildInputs.addBoolValueInput('_autoroute', 'AutoRoute', False, '', True)
            # Create bool value input with button style to create DFX file
            tab1ChildInputs.addBoolValueInput('_DXF', 'Save Tracers', False, '', True)
            # Create bool value input with button style to create cavities for components
            tab1ChildInputs.addBoolValueInput('_cavity', 'Create Cavities', False, '', True)

            
            for n in range(0, len(SelectedFiles)):
                    table = tab1ChildInputs.addTableCommandInput('_table'+str(n), str(SelectedFiles[n]), 2, '1:1')
                    #table = adsk.core.TableCommandInput.cast(inputss.addTableCommandInput('_table'+str(n), str(SelectedFiles[n]), 2, '1:1'))
                    table.minimumVisibleRows = 0
                    table.maximumVisibleRows = len(SelectedFiles)
                    table.columnSpacing = 1
                    table.rowSpacing = 1
                    table.tablePresentationStyle = adsk.core.TablePresentationStyles.itemBorderTablePresentationStyle
                    table.hasGrid = True

                    selectionInput = tab1ChildInputs.addSelectionInput('_selection'+str(n), 'Selection: '+str(SelectedFiles[n]), '_selection'+str(n))
                    selectionInput.setSelectionLimits(1, 1)
                    selectionInput.addSelectionFilter('ConstructionPlanes');                    
            
            
            for n in range(0, len(SelectedFiles)):
                table = inputss.itemById('_table'+str(n))
                text = inputss.addTextBoxCommandInput('_textBox'+str(n), 'Text Box'+str(n), '', 1, True)
                text.text = str(SelectedFiles[n])
                text.isReadOnly = True
                table.addCommandInput(text, n, 0, False, False)

                text = inputss.addTextBoxCommandInput('_planeOn'+str(n), 'PlaneOn'+str(n), '', 1, True)
                text.text = "The selected Construction Plane's information will be displayed here."
                text.isReadOnly = True
                table.addCommandInput(text, n, 1, False, False)
                    
                    
            
            
                #table = tab1ChildInputs.itemById('_table'+str(n))
                #table.addCommandInput(table.commandInputs.addTextBoxCommandInput('_textBox'+str(n), 'Text Box'+str(n), str(SelectedFiles[n]), 1, True), n, 0)
                #table.addCommandInput(table.commandInputs.addTextBoxCommandInput('_planeOn'+str(n), 'PlaneOn'+str(n), "Hello World", 1, True), n, 1)
                    
            
                        
            # Connect to the execute event.
            onExecute = CommandExecuteHandler()
            cmd.execute.add(onExecute)
            handlers.append(onExecute)
            
            onInputChanged = UTEPMultiProcessButtonPressedCommandInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            handlers.append(onInputChanged)
            
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
class CommandExecuteHandler(adsk.core.CommandEventHandler):
        def __init__(self):
            super().__init__()
        def notify(self, args):
            try:
                app = adsk.core.Application.get()
                ui = app.userInterface
                
                selectedCPs = []
                dirs =[]
                files = []
                
                for n in range(0, len(SelectedFiles)):
                    currentSelectionInput = tab1ChildInputs.itemById('_selection'+str(n))
                    currentSelectionInput.isEnabled = False
                    if currentSelectionInput.selectionCount == 1:
                        selectedCPs.append(currentSelectionInput)
                        dirs.append(directories[n])
                        files.append(SelectedFiles[n])
                
                if(buttonClicked == "_place"):
                    
                    for n in range(0, len(selectedCPs)):
                            #USING CONSTRUCTION PLANES RIGHT NOW
                            ConstructionPlane = selectedCPs[n].selection(0).entity
                            extensionInput = tab1ChildInputs.itemById('_extension')
                            pinExtension = extensionInput.value
                            pinExtension = pinExtension*10.0 #converting from cm to mm
                            #selectedCPs.append(ConstructionPlane)
                            #schematicFilesofCPs.append(SelectedFiles(n))
                            
                            directory = dirs[n]
                            file_name = files[n]

                            Nets, Components = CC.run(directory, file_name)
 
                            ui.messageBox("Nets and Components have been extracted: \n  Nets length: " + Str(length(Nets)))

                            sizes_warning(Nets)

                            #here, call untitled0.py run() but before, get the Xs, Ys and Zs of construction plane.
                            ui.messageBox("After CC and warnings, now calling sketch")

                            CS.run(contextt, file_name, pinExtension, Nets, Components)
                            
                                
                elif(buttonClicked == "_autoroute"):
                    for n in range(0, len(selectedCPs)):
                        ConstructionPlane = selectedCPs[n].selection(0).entity
                        directory = dirs[n]
                        file_name = files[n]
                        Nets = NIE.run(directory, file_name)
                        CREATEMAP.run(contextt, Nets, ConstructionPlane)
                    
                elif(buttonClicked == "_cavity"):
                    for n in range(0, len(selectedCPs)):
                        directory = dirs[n]
                        file_name = files[n]
                        Names = []
                        CrossHairs = []
                        Xs = []
                        Ys = []
                        Heights = []
                        Pins = []
                        
                        Names, CrossHairs, Xs, Ys, Heights, Pins = SIE.run(directory, FILE)
                    CAV.MakeCavities(Heights)
                elif(buttonClicked == "_DXF"):
                    product = app.activeProduct
                    design = adsk.fusion.Design.cast(product)
                    model = design.activeComponent
                    sketches = model.sketches
                    n = 0
                    for s in range(0, sketches.count):
                        if("Tracer" in str(sketches.item(s).name)):
                            dirName = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
                            filename = dirName + '\\'+"Tracers"+str(n)+".dxf"
                            saved = sketches.item(s).saveAsDXF(filename)
                            if(saved):
                                ui.messageBox("The file has been saved as a .dxf file at address: "+str(filename))
                            n = n + 1
            except:
                if ui:
                    ui.messageBox(('command executed failed: {}').format(traceback.format_exc()))


def sizes_warning(Nets):
    
    nets_with_incompatible_pins = []
    for netName, pinList in Nets.items():

        for i in range(len(pinList)):
           
            outer_component = pinList[i]['component']
            if outer_component !="GND" or outer_component != "VCC": 
                
                for j in range(i+1, len(pinList)): 

                    inner_component = pinList[j]['component']
                    if inner_component != "GND" or inner_component != "VCC": 

                        first_ID = pinList[i]['ID']
                        first_gauge = pinList[i]['gauge'] 

                        second_ID = pinList[j]['ID']
                        second_gauge = pinList[j]['gauge'] 

                        if first_gauge != None or first_gauge != None:

                            '''
                            The difference is calculated to determine if it is great enough to cause 
                            compatibility issues. If a specific threshold is ever determined, then 
                            some gauge differences can be overlooked. 
                            '''
                            difference = round(abs(float(first_gauge) - float(second_gauge)), 2)

                            if abs(difference) > .10 :

                                nets_with_incompatible_pins.append(netName) 
   
    if len(nets_with_incompatible_pins): 
        error_message = "There might be compatibility issues between the following interconnected pins due to their gauge sizes: \n"
        
        for current_net in nets_with_incompatible_pins: 
            error_message += "\n" + "Incompatible Grouped Pins: " + str(i) + "\n" 
            
            for pin in Nets[current_net]: 
                pin_gauge = str(pin['gauge'])
                component_pin = pin['ID'].split('_')
                component_name = component_pin[0]
                pin_name = component_pin[1] 

                error_message += "Component: " + component_name + "  Pin: " + component_pin +  "  Gauge size: " + pin_gauge + "\n"

def run(context, slctFiles, dirs):
    ui = None
    try:
        global app
        app = adsk.core.Application.get()
        global ui
        ui = app.userInterface
        #ui.messageBox("HELLO WORLD")
        global contextt
        contextt = context
        global SelectedFiles
        SelectedFiles = slctFiles
        global directories
        directories = dirs

        global commandId
        global commandName
        global commandDescription

        # Create command defintion
        cmdDef = ui.commandDefinitions.itemById(commandId)
        if not cmdDef:
            cmdDef = ui.commandDefinitions.addButtonDefinition(commandId, commandName, commandDescription)
        
        #R.run(contextt)
        # Add command created event
        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        # Keep the handler referenced beyond this function
        handlers.append(onCommandCreated)

        # Execute command
        cmdDef.execute()

        # Prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        #docu = app.activeDocument
        #datafolder = adsk.core.DataFolder
        #ui.messageBox("Has this file been saved before? "+str(docu.isSaved))
        #docu.saveAs("hello", datafolder.parentFolder,"","")
        
        #if(saved == True):
        #    ui.messageBox("File was successfully saved!!!")
        #if(saved == False):
        #    ui.messageBox("File failed to save.")
        adsk.autoTerminate(False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


