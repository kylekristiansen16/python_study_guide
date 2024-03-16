
# class methods
# Class methods are methods that, like class variables, work on the class itself, and not on the class objects that are instantiated. 
# You can say that they are methods bound to the class, not to the object.
#   1 we control access to class variables, e.g., to a class variable containing information about the number of created instances or the 
#           serial number given to the last produced object, or we modify the state of the class variables;
#   2 we need to create a class instance in an alternative way, so the class method can be implemented by an alternative constructor.
# the init method cannot receive cls as a parameter, as it is called before the object is created, and therefore, before the class is known.
#   it can only reference the class by its name, not by a variable containing the class name.

""" 
tool methods available to all class instances
"""

class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())

# extending constructors

class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called :', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand): # offers an alternative constructor for the class
        print('Class method was called')
        _car = cls(vin) # calls the __init__ method
        _car.brand = brand # adds new attributes to the class instance
        return _car # returns the class instance

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand) # no brand to retrieve because it was instantiated the normal way
print(car2.vin, car2.brand)