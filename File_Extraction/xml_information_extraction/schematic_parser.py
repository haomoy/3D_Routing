import adsk.core, adsk.fusion, adsk.cam, traceback
from xml.etree import ElementTree as ET
from xml.dom import minidom

def run(directory, filename):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        #fPath = inspect.getfile(inspect.currentframe())
        #inputFile = "cloudv7.sch"
        dirname = str(directory + filename)
        dirname = dirname.replace("/", "\\")
        e = ET.parse(dirname)
        #root = e.getroot()
        
        outputFile = dirname[:len(dirname)-4]+"_output_XML.xml"
        ##############################################################################
        '''
        Find Perimieter Layer Method
        '''
        p_layers = []
        for layer in e.iter('layer'):
            if layer.get('name') == 'Perimeter':
                p_layers.append(layer.get('number'))
        ##############################################################################

        ##############################################################################
        '''
        Build part dictionary for references
        '''
        part_dict = {}
        for ps in e.iter('parts'):
            for p in ps.iter('part'):
                ref = p.get('name')
                device = p.get('deviceset')
                part_dict[ref] = device

        part_dict_inv = dict([[v,k] for k,v in part_dict.items()])

        '''
        DEBUG, DELETE EVENTUALLY
        '''
        display = " " 
        for k,v in part_dict_inv.items(): 
            display = display + "\n" + str(k) + ": " + str(v)
        ui.messageBox("Part Dict \n" + str(display))
        
        height_dict = {}
        for deviceset in e.iter('deviceset'):
            name = deviceset.get('name')
            if name in part_dict_inv.keys():
                for attribute in deviceset.iter('attribute'):
                    if attribute.get('name'):
                        height_dict[name] = attribute.get('value')
        
        '''
        DEBUG, DELETE EVENTUALLY
        '''
        display = " " 
        for k,v in height_dict.items(): 
            display = display + "\n" + str(k) + ": " + str(v)
        ui.messageBox("Height Dict \n " + str(display))
                        
        ##############################################################################

        ##############################################################################
        root_out = ET.Element('Schematic')

        components_out = ET.SubElement(root_out, 'Components')
        '''
        make list of symbols
        '''
        symbols = []
        for symbol in e.iter('symbol'):
            component = 0
            for wire in symbol.iter('wire'):
                if wire.get('layer') in p_layers:
                    component = 1
                    break
            if component:
                symbols.append(symbol)

        '''
        DEBUG, DELETE EVENTUALLY
        '''
        display = " " 
        for k in symbols: 
            display = display + "\n" + str(k)
        ui.messageBox("Sybmols \n " + str(display))

        '''
        Collect Pin wire gauges
        '''
        #Pin thicknesses are contained in package portion of .sch
        parts_wire = {}
        for package in e.iter('package'):
            package_name = package.get('name')
            thickness = {}
            for smd in package.iter('smd'):
                smd_name = smd.get('name')
                dx = smd.get('dx')
                dy = smd.get('dy')
                thickness[smd_name] = dy
            for pad in package.iter('pad'):
                pad_name = pad.get('name')
                drill = pad.get('drill')
                thickness[pad_name] = drill
            parts_wire[package_name] = thickness
        
        '''
        DEBUG, DELETE EVENTUALLY
        '''
        display = " " 
        for k,v in parts_wire.items(): 
            display = display + "\n" + str(k) + ": " + str(v)
        ui.messageBox("Parts Wire \n " + str(display))
        
        #Pin names retrieved from pacakge portion must be translated using device portion
        parts_wire_ref = {}
        for device in e.iter('device'):
            device_name = device.get('package')
            pin_ref = {}
            for connect in device.iter('connect'):
                pin_name = connect.get('pin')
                pad_name = connect.get('pad')
                pin_ref[pin_name] = pad_name
            parts_wire_ref[device_name] = pin_ref
            
        '''
        DEBUG, DELETE EVENTUALLY
        '''
        display = " " 
        for k,v in parts_wire_ref.items(): 
            display = display + "\n" + str(k) + ": " + str(v)
        ui.messageBox("Parts Wire Ref \n " + str(display))
            
        '''
        Compile Pin information for each component
        '''
        #clean up found symbols        
        for symbol in symbols:
            symbol_out = ET.SubElement(components_out, 'Component')
            symbol_out.set('name', symbol.get('name'))
            symbol_out.set('height', height_dict[symbol.get('name')])
            
            instance_out = ET.SubElement(symbol_out, 'Instance')
            for instance in e.iter('instance'):
                if instance.get('part') == part_dict_inv[symbol.get('name')]:
                    jhk = instance.attrib
                    for attribute, value in instance.attrib.items():
                        instance_out.set(attribute, value)
                        
            perimeter = ET.SubElement(symbol_out, 'Perimeter')
            for wire in symbol.iter('wire'):
                if wire.get('layer') in p_layers:
                    perimeter.append(wire)

            wire_thick = parts_wire[symbol.get('name')]  
            pin_names = parts_wire_ref[symbol.get('name')]      
            pins = ET.SubElement(symbol_out, 'Pins')
            for pin in symbol.iter('pin'):    
                pin.set('gauge', wire_thick[pin_names[pin.get('name')]])
                pins.append(pin)
                 
        '''
        Compile Net information
        ''' 
        #Make Nets
        nets_out= ET.SubElement(root_out,'Nets')
        for net in e.iter('net'):
            net_out = ET.SubElement(nets_out, 'Net')
            net_out.set('name', net.get('name'))
            
            for segment in net.iter('segment'):
                    pins = []
                    for pinref in segment.iter('pinref'):
                        
                        pin = ET.SubElement(net_out, 'Pin')
                        ref = pinref.get('part')
                        partname = part_dict[ref]
                        name = pinref.get('pin')
                        pin.set('name', name)
                        pin.set('component', partname)
            
        ##############################################################################

        ##############################################################################
        '''
        Output file pretty
        '''
        final_xml = minidom.parseString(ET.tostring(root_out)).toprettyxml()
        text = "".join([s for s in final_xml.splitlines(True) if s.strip("\t\r\n")])
        with open(outputFile,"w+") as f:    
            f.write(text)
            f.close
        ##############################################################################
           
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
