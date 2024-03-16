
""" 
XML = eXtendable Markup Language
    eXtenable: you can define your own tags
    Markup: it's a language for marking up text
    Language: it's a language, not a data format

XML is a language - universal and transparent carrier
- invented before JSON
- invented for the same reason as JSON, but so different

Each XML document contains...
    - a header (optional)
    - a root element (mandatory) and only exactly one
    - any (including 0) number of child elements
    - any (including 0) number of attributes
    - any (including 0) number of comments
    - any (including 0) number of processing instructions

doc:

<?xml version = "1.0" encoding = "utf-8"?>          # declares that the document contains XML text
<!-- cars.xml - List of cars ready to sell -->      # a comment. It means nothing. The XML parser will ignore it completely
<!DOCTYPE cars_for_sale SYSTEM "cars.dtd">          # defines the document type. NAME [SYSTEM | PUBLIC] "URI"
<cars_for_sale>                                     # root element
   <car>                                            # child element #1
      <id>1</id>                                    # element content (attributes)
      <brand>Ford</brand>
      <model>Mustang</model>
      <production_year>1972</production_year>
      <price currency="USD">35900</price>           # element attribute CURRENCY is defined inside tag 
   </car>
   <car>                                            # child element #2          
      <id>2</id>
      <brand>Aston Martin</brand>
      <model>Rapide</model>
      <production_year>2010</production_year>
      <price currency="GBP">32000</price>
   </car>
</cars_for_sale>

notes:
- has a header, uses attribute = value pairs, version and encoding, a program responsible for parsing a file’s content knows what to expect next
- comments are ignored by the parser, signified by <!-- and -->
- documents can be self-defining or specified by a DTD (Document Type Definition - metadata about the XML document)
- DTDs are a document describing the structure of an XML document
- XML document consists of elements. Each element is marked by a pair of tags: an opening tag and a closing tag
- <empty/> is an empty element, no closing tag
- XML allows us to put as many attributes inside a tag as we need

how to parse XML in Python?
- tree (graph) structure

cars_for_sale
|
|____ car
|     |_ id:1
        |_ brand: Ford
        |_ model: Mustang
        |_ production_year: 1972
        |_ price(USD): 35900
|
|____ car
	|_ id:2
	   |_ brand: Aston Martin
	   |_ model: Rapide
	   |_ production_year: 2010
	   |_ price(GPB): 32500
"""

import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('/Users/kylekristiansen/cherreco/python/04_restful_apis/05_XML/cars.xml')
cars_for_sale = tree.getroot() 
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        if prop.tag == 'price':
            print('\t\t', prop.tag, prop.attrib, end='')
        else:
            print('\t\t', prop.tag)
    print(' =', prop.text)

print()

for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4' # each invocation needs two arguments: a parent element object (new_car here) and a sub-element name (as a string)
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='')
print('wrote newcars.xml')

# most currently implemented services use JSON, not XML. 
# It's highly possible that you may encounter a server which implements communication on exchanging XML documents, but JSON is much more popular.