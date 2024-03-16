import xml.etree.ElementTree as ET

tree = ET.parse('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    
    child.remove(child.find('author'))  # remove attributes using find method
    child.remove(child.find('year'))
    
    child.set('rate', '5')  # just like get, you can set attributes using set method
    
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/movies.xml', 'UTF-8', True)