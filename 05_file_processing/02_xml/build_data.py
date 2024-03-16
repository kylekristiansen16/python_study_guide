import xml.etree.ElementTree as ET

root = ET.Element('data')  # create root element, args are tag & attrib dict
ET.dump(root)  # dump is a method that prints the xml tree

print()

""" 
SubElement - function for creating child elements
- first one defines the parent element, 
- the second one defines the tag name, 
- the third (optional) defines the attributes of the element. 
"""
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})  # parent, tag, attributes | notice no text!!
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})

""" 
To save a document using the write method, we need to have an ElementTree object. 
To do this, pass our root element to its constructor:
    tree = ET.ElementTree(root)
"""

tree = ET.ElementTree(root)

tree.write('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/data.xml', 'UTF-8', True)
