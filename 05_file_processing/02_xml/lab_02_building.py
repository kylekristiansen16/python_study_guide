
""" 
improving the student's skills in building an XML document;
using the Element class and the SubElement function.

You are a programmer working for an online store. Your task is to build an XML document containing 
information about the three vegan products available in the store:

<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>

Save the document to the shop.xml file. Use UTF-8 character encoding and don't forget to add the 
prolog to the beginning of the file. Good luck!
"""

import xml.etree.ElementTree as ET

root = ET.Element('shop')

category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

product_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
product_1_type = ET.SubElement(product_1, 'type')
product_1_type.text = 'cereals'  # notice how we can set the text of the element using the text attribute
product_1_producer = ET.SubElement(product_1, 'producer')
product_1_producer.text = 'OpenEDG Testing Service'
product_1_price = ET.SubElement(product_1, 'price')
product_1_price.text = '9.90'
product_1_currency = ET.SubElement(product_1, 'currency')
product_1_currency.text = 'USD'

product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
product_2_type = ET.SubElement(product_2, 'type')
product_2_type.text = 'pasta'
product_2_producer = ET.SubElement(product_2, 'producer')
product_2_producer.text = 'Programmers Eat Pasta'
product_2_price = ET.SubElement(product_2, 'price')
product_2_price.text = '15.49'
product_2_currency = ET.SubElement(product_2, 'currency')
product_2_currency.text = 'EUR'

product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})
product_3_type = ET.SubElement(product_3, 'type')
product_3_type.text = 'beverages'
product_3_producer = ET.SubElement(product_3, 'producer')
product_3_producer.text = 'Drinks4Coders Inc.'
product_3_price = ET.SubElement(product_3, 'price')
product_3_price.text = '19.75'
product_3_currency = ET.SubElement(product_3, 'currency')
product_3_currency.text = 'USD'

product_4 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})
product_4_type = ET.SubElement(product_4, 'type', {'attrib': 'example'}, text='cereal')  # not possible to set text value in SubElement function
product_4_producer = ET.SubElement(product_4, 'producer', {}, text='cheerios')

tree = ET.ElementTree(root)

tree.write('/Users/kylekristiansen/cherreco/python/05_file_processing/02_xml/lab_02_shop.xml', 'UTF-8', True)

