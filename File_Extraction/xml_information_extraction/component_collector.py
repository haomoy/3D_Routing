
import adsk.core, adsk.fusion, adsk.cam
from xml.etree import ElementTree as ET
from copy import deepcopy
global app
global ui
app = adsk.core.Application.get()
ui = app.userInterface

def run(directory, filename):
    
    directory_name = directory
    directory_name = directory_name + filename[:len(filename)-4] + "_output_XML.xml"
    e = ET.parse(directory_name)

    components = {}
    nets = {}
    pin_length_reference = {'short': 2.54, 'middle': 5.08, 'long': 7.62}
    
    for component in e.iter('Component'):
        component_name = component.get('name')
        heigth = component.get('height')
        
        Instance = component[0]
        Perimeter = component[1]
        Pins = component[2]
        
        crosshair = (Instance.get('x'), Instance.get('y'))
        
        cnt_value = component.get('cnt') if component.get('cnt') else 0
        component_rot = Instance.get('rot') if Instance.get('rot') else "R0"
        
        component_coordinates = {'x':[], 'y':[]}
        
        for wire in Perimeter:
            component_coordinates['x'].append(wire.get('x1'))  
            component_coordinates['x'].append(wire.get('x2'))  
            component_coordinates['y'].append(wire.get('y1'))  
            component_coordinates['y'].append(wire.get('y2'))  
        
      
        component_pins = {}
        for pin in Pins:
            pin_name = str(pin.get('name'))
            pin_ID = component_name + "_" + pin_name
            gauge = pin.get('gauge')
            pin_coordinates = (pin.get('x'), pin.get('y'))
            pin_rot = pin.get('rot') if pin.get('rot') else "R0"
            pin_length = pin_length_reference[pin.get('length')]
            
            component_pins[pin_name] = {'ID': pin_ID, 'gauge': gauge, 'coordinates': pin_coordinates, 
                          'rot': pin_rot, 'length': pin_length, 'component': component_name}
            
            
        components[component_name] = {'heigth': heigth, 'crosshair': crosshair, 'cnt': cnt_value, 'rot': component_rot,
                  'coordinates': component_coordinates, 'pins': component_pins} 
        
    '''   
    for name_component, component_characteristic in components.items(): 
        print(" ")
        print("###################################")
        print("Component name: " + name_component)
        print("     Heigth: " + str(component_characteristic["heigth"]))
        print("     CrossHair: " + str(component_characteristic["crosshair"]))  
        print("     CNT: " + str(component_characteristic["cnt"]))  
        print("     Rot: " + str(component_characteristic["rot"]))
        print("     Coordinates: " + str(component_characteristic["coordinates"]))  
        print("     Pins: ")  
        for name_pin, pin_characteristics in component_characteristic['pins'].items():
            print("          Pin name: " + name_pin)  
            print("          ID: " + str(pin_characteristics["ID"]))  
            print("          gauge: " + str(pin_characteristics["gauge"]))  
            print("          coordinates: " + str(pin_characteristics["coordinates"]))
            print("          rot: " + str(pin_characteristics["rot"]))
            print("          length: " + str(pin_characteristics["length"]))
            print(" ")
    '''
     
    for net in e.iter('Net'):
        net_name = net.get('name')
        print("##################################")
        print("Current net: " + net_name)
        current_net_pins = []
        
        for pin in net.iter('Pin'):
            pin_component = pin.get('component')
            if pin_component not in ['VCC', 'GND']: 
                pin_name = str(pin.get('name'))
                print("     Pin component: " + pin_component)
                print("     Pin name: " + pin_name)
                current_net_pins.append(deepcopy(components[pin_component]['pins'][pin_name]))
            
        nets[net_name] = current_net_pins
        
   
    ui.messageBox("Returning from component_collector")
    
    
    return nets, components 
