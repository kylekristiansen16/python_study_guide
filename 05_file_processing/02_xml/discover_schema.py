import xml.etree.ElementTree as ET
from pprint import pprint

def discover_schema(element, parent_path='', schema=None):
    if not schema:
        schema = {}
        schema[element.tag] = element.text
        parent_path = element.tag
        
    for child in element:        
        path = parent_path + '.' + child.tag
        if path not in schema:
            schema[path] = child.text
            
        discover_schema(child, path, schema)
    return schema
 
tree = ET.parse('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/lab_02_shop.xml')
root = tree.getroot()  # returns object of Element class

unpacked_schema = discover_schema(root)

pprint(unpacked_schema)
