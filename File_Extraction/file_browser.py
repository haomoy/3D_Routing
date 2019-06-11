"""
@author: htmoy
"""

import adsk.core, adsk.fusion, adsk.cam, traceback
import tkinter as tk
import os
import inspect
from .xml_information_extraction import schematic_parser as OSP


def run(context):
    try:
        selectedFiles = []
        app = adsk.core.Application.get()
        ui  = app.userInterface
        fileDialog = ui.createFileDialog()
        fileDialog.isMultiSelectEnabled = True
        fileDialog.title = "Select .sch file"
        fileDialog.filter = 'Jason files (*.sch)'
        fileDialog.filterIndex = 0
        dirName = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        
        fileDialog.initialDirectory = dirName
        fileDialog.showOpen()
        root = tk.Tk()
        root.withdraw()
        selectedFiles.append(fileDialog.filenames)
        files = selectedFiles[0]
        for j in range(0, len(files)):
            tempName = files[j]
            indexOfLastSlash = 0
            for i in range(0, len(tempName)):
                if(tempName[i] == "/"):
                    indexOfLastSlash = i+1        
            fileName = tempName[indexOfLastSlash:]
            directory = tempName[0:indexOfLastSlash]
            OSP.run(directory, fileName)
            
        return selectedFiles
        
    except ValueError:
        print("Parser script did not run...")