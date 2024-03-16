""" 
polymorphism is the provision of a single interface to objects of different types. 
In other words, it is the ability to create abstract methods from specific types in order to treat those types in a uniform way.
- Imagine that you have to print a string or an integer — it is more convenient when a function is called simply print, not print_string or print_integer.

!polymorphism is the same function handling different types of objects!

Duck typing is a fancy name for the term describing an application of the duck test: 
"If it walks like a duck and it quacks like a duck, then it must be a duck", 
which determines whether an object can be used for a particular purpose. 
An object's suitability is determined by the presence of certain attributes, rather than by the type of the object itself.

polymorphism is used when different class objects share conceptually similar methods (but are not always inherited)
polymorphism leverages clarity and expressiveness of the application design and development;
when polymorphism is assumed, it is wise to handle exceptions that could pop up.

aka.... polymorphism is giving the same name to methods that do different things
"""

dir(1)
dir('a')

a = 10
print(a.__add__(20))
b = 'abc'
print(b.__add__('def')) # polymorphism because the same __add__ method is used for both int and str

class Device:
    def turn_on(self):
        print('The device was turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()