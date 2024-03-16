
xml_string = """ 
<library>
    <book>
        <title> Book1 </title>
        <author> Author1 </author>
    </book>
    <book>
        <title> Book2 </title>
        <author> Author2 </author>
    </book>
    <book>
        <title> Book3 </title>
        <author> Author1 </author>
    </book>
</library>
"""

import xml.etree.ElementTree as ET
root = ET.fromstring(xml_string)
print(root.tag)
print(root)

print()

titles = [elem.text 
          for elem in root.findall('./book[author="Author1"]/../title')]
# titles = [elem.text 
#           for elem in root.findall('./book/author="Author1"/title')]
titles = [elem.text 
          for elem in root.findall('./book[author="Author1"]/../title')]
print(titles)