
""" 
3 modules for working with XML:
- xml.etree.ElementTree – has a very simple API for analyzing and creating XML data. It's an excellent choice
    for people who have never worked with the Document Object Model (DOM) before.
- xml.dom.minidom – is the minimum implementation of the Document Object Model (DOM). Using the DOM, the
    approach to an XML document is slightly different, because it's parsed into a tree structure in which each node 
    is an object.
- xml.sax – SAX is an acronym for “Simple API for XML”. SAX is an interface in Python for event-driven XML
    document analysis. Unlike the above modules, analyzing a simple XML document using this module requires more work.

xml 
- used for storing & transporting data
- on systems using SOAP protocol

every xml doc contains:
- prolog – the first (optional) line of the document. In the prolog, you can specify character encoding, e.g., 
    <?xml version="1.0" encoding="ISO-8859-2"?> changes the default character encoding (UTF-8) to ISO-8859-2.
- root element – the XML document must have one root element that contains all other elements. In the example 
    below, the main element is the data tag.
- elements – these consist of opening and closing tags. The elements include text, attributes, and other child 
    elements. In the example below, we can find the book element with the title attribute and two child elements 
    (author and year).
- attributes – these are placed in the opening tags. They consist of key-value pairs, e.g., title = "The Little 
    Prince".
    
utf-8 is the default encoding for xml files
3 modules:
- xml.etree.ElementTree
- xml.dom.minidom
- xml.sax
standard elements:
- prolog (version & character encoding)
- root element (contains all other elements)
- elements (opening & closing tags)
- attributes (key-value pairs in opening tags) optional

"""