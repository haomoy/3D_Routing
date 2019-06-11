#Description-
import adsk.core, adsk.fusion, adsk.cam, traceback
import ctypes
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from .UTEPGuiModules import Browse as B
from .UTEPGuiModules import Reference1 as R
from .UTEPGuiModules import ComponentList as CL
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
commandName = 'UTEP Fusion 360 GUI'
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
                ui.messageBox("Here are the following steps and descriptions the user should take to work properly with a working design: \n\n1. After activating a reference, click BROWSE to open a file dialog. Select as many schematic (.sch) files as you want, then select OPEN. \n\n2. Afterwards, a new tab is created in the Gui. In the new tab, there will be a list of the schematic files selected. Click on HELP on that tab for more information. \n\n3. Click the CREATE REFERENCE button first or last to have as a dimensional reference for your future design.\n \n\n GENERAL DESCRIPTIONS of each function: \n\nCREATE REFERENCE - creates a reference where you may look as reference placement for your design.\n\nBROWSE - It parses a schematic file from EAGLE, takes the dimension of components and saves them in a new text file. Then it will create a tab with the component list that is linked to the dimensions from the created text file")
            
            if cmdInput.id == '_reference':
                buttonClicked = "_reference"
                action = cmd.doExecute(False)
                buttonClicked = ""
        
            if cmdInput.id == '_browse':
                temp = B.run(contextt)
                files = temp[0]
                
                for j in range(0, len(files)):#for every selected file, get the file name and append it to list
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
            
            
            #help
            tab1ChildInputs.addBoolValueInput('_help', 'Help', False, '', True)
            # Create bool value input with button style
            tab1ChildInputs.addBoolValueInput('_browse', 'Browse', False, '', True)
            # Create bool value input with button style # reference
            tab1ChildInputs.addBoolValueInput('_reference', 'Create Reference', False, '', True)
            
                        
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
                    CL.run(contextt, selectedFiles, directories)
                    #COWS.run(contextt, inputss, selectedFiles)
                if buttonClicked == "_reference":
                    R.CreateReference2()
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
