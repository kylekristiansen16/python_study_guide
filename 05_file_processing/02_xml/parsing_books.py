# one module for parsing an element tree
import xml.etree.ElementTree as ET 

tree = ET.parse('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/books.xml')
# can also use ET.fromstring() to parse from a string
root = tree.getroot()  # returns object of Element class

print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)  # tag = name as string, attrib = dict of attributes

print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)  # book[0] is the first child element of book
    print('Year: ', book[1].text, '\n')  # it's okay to use index here because we know the order of the elements/

# write a method to discover the schema of the books xml file
print()

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

unpacked_schema = discover_schema(root)

from pprint import pprint
pprint(unpacked_schema)