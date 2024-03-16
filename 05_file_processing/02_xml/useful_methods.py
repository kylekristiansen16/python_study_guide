
import xml.etree.ElementTree as ET 

tree = ET.parse('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/books.xml')  # open with a parse
root = tree.getroot()  # returns object of Element class

""" 
iter method returns all elements by having the tag passed as an argument
The element that calls it is treated as the main element from which the search starts

recursive search through all child elements and sub-elements
"""
for author in root.iter('author'):  # use when you're looking for an element name that might be nested
    print(author.text)
    
""" 
findall to search for direct child elements. 
Unlike the iter method, the findall method only searches the children at the first nesting level.
"""
for author in root.findall('author'):  # use when you're looking for a child element name
    print(author.text)  # doesn't return any results bc findall can only iterate over the book elements
    
""" 
to display the value of the title attributes, we use the get method, 
which looks much better than a book.attrib ['title']

get() has optional 2nd argument that returns the value of the attribute if it's not found
"""
for book in root.findall('book'):
    print(book.get('title'))  # returns the title attribute of each book element
    
""" 
find method returns the first child element containing the specified tag or matching XPath expression
"""

print(root.find('book').get('title'))  # find the first child element containing the book tag
