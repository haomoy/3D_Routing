#Author-Hao Moy 
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
from .File_Extraction import file_browser as Browse         
from .Reference_Geometry import regular_reference as Reference   
from .Mapping import map_generator as Mapping    
#from .UTEPGuiModules import ComponentList as CL   
handlers = []
global selectedFiles
selectedFiles = []
global directories
directories = []
global constructionPlanes
constructionPlanes = []
global selectedPlanes
selectedPlanes = []

app = None
ui  = None
commandId = 'CommandInputGallery'
commandName = 'UTEP Embedding Gui'                         
commandDescription = 'Demo command input examples.'
rowNumber = 0

# Global set of event handlers to keep them referenced for the duration of the command
handlers = []


# Event handler for the execute event.
class ButtonPressedHandler(adsk.core.InputChangedEventHandler):
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
            buttonClicked = ""
        
            #selectInput = selectionArgs.id
            #ui.messageBox("SelectionEvent: "+str(selectInput))
            
            if cmdInput.id == '_help':
                ui.messageBox('''
Tab Overview: 
This Add-Inn allows you to select an EAGLE 360 schematic file and translate their components into Fusion 360 Sketches.  

Browse: 
This button opens File Explorer, allowing you to select the EAGLE schematic file to be translated.
After file(s) are selected, a new tab will appear next to "UTEP Gui". 
This tab also contains a Help button to guide you through the software. 

Create Reference: 
This button creates a shape to be used as geometric reference on the printing bed.
If unsure of what this means you can press it, it will not interfere or modify your current work.
''')
                
            if cmdInput.id == '_reference':
                buttonClicked = '_reference'
                action = cmd.doExecute(False)
                buttonClicked = ""

            if cmdInput.id == '_browse':
                temp = Browse.run(contextt)
                files = temp[0]
                
                #for every selected file, get the file name and append it to list
                for j in range(0, len(files)):
                    tempName = files[j]
                    indexOfLastSlash = 0
                    for i in range(0, len(tempName)):
                        if(tempName[i] == "/"):
                            indexOfLastSlash = i+1        
                    filename = tempName[indexOfLastSlash:]
                    directories.append(tempName[0:indexOfLastSlash])
                    selectedFiles.append(filename)
                buttonClicked = '_browse'
                action = cmd.doExecute(False)
                buttonClicked = ""
                
            '''
            #############################
            Temporal button to display bounding box
            #############################
            '''
            if cmdInput.id == '_map':
                Mapping.run(contextt)
                buttonClicked = '_map'
                buttonClicked = ""
                
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
            tabCmdInput1 = inputss.addTabCommandInput(commandId + '_table_1', 'UTEP Gui')
            global tab1ChildInputs            
            tab1ChildInputs = tabCmdInput1.children
            
            
            # Help
            tab1ChildInputs.addBoolValueInput('_help', 'Help', False, '', True)
            # Create bool value input with button style to browse
            tab1ChildInputs.addBoolValueInput('_browse', 'Browse', False, '', True)
            # Create bool value input with button style for reference
            tab1ChildInputs.addBoolValueInput('_reference', 'Create Reference', False, '', True)
            
            '''
            #############################
            Temporal button to display bounding box
            #############################
            '''
            # Create bool value input with button style for temporal 
            tab1ChildInputs.addBoolValueInput('_map', 'Create Bounding Box', False, '', True)
            
            
                        
            # Connect to the execute event.
            onExecute = CommandExecuteHandler()
            cmd.execute.add(onExecute)
            handlers.append(onExecute)
            
            onInputChanged = ButtonPressedHandler()
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
                #ui.messageBox("inside execute handler")
                command = args.firingEvent.sender
                if buttonClicked == '_browse':
                    #ui.messageBox("inside if browse statement")
                    
                    '''
                    #################################################################################################
                    REPLACE WITH YOUR COMPONENT LIST FILE
                    CL.run(contextt, selectedFiles, directories)
                    #################################################################################################
                    '''
                    
                    #COWS.run(contextt, inputss, selectedFiles)
                if buttonClicked == "_reference":
                    Reference.CreateReference2()
                #if buttonClicked == "_place":
                #    P.PlaceComponents(contextt, )
                
            except:
                if ui:
                    ui.messageBox(('command executed failed: {}').format(traceback.format_exc()))

def run(context):
    ui = None
    try:
        global app
        app = adsk.core.Application.get()
        global ui
        ui = app.userInterface
        global contextt
        contextt = context

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