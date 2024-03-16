""" 
Metaprogramming is a programming technique in which computer programs have the ability to modify their own or other programs’ codes

!in metaprogramming, programs can treat other programs as their data!and modify their own code!

this technique could be used for tool preparation; those tools could be applied to your code to make it follow specific programming patterns, or to help you create a coherent API 

example of metaprogramming is the metaclass concept
    Tim Peters: "if you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why)"

metaclass is a class whose instances are classes, similar but different from decorators because
    decorators bind the names of decorated functions or classes to new callable objects. Class decorators are applied when classes are instantiated;
    metaclasses redirect class instantiations to dedicated logic, contained in metaclasses. Metaclasses are applied when class definitions are read to 
        create classes, well before classes are instantiated.

The typical use cases for metaclasses:
    - logging;
    - registering classes at creation time;
    - interface checking; -- seems powerful
    - automatically adding new methods;
    - automatically adding new variables.
"""

class Dog:
    pass


age = 10
codes = [33, 92]
dog = Dog()

print(type(age))    # <class 'int'>
print(type(codes))  # <class 'list'>
print(type(dog))    # <class '__main__.Dog'>
print(type(Dog))    # <class 'type'>

# type is the default metaclass responsible for creating all the classes in Python
print()

for t in (int, list, type): # all of class 'type'
    print(type(t))
    
# <class object> is an instance of <class> is an instance of <metaclass>

""" 
special class attributes:
    __name__ – inherent for classes; contains the name of the class;
    __class__ – inherent for both classes and instances; contains information about the class to which a class instance belongs;
        class definitions belong to their metaclass class, which is why they return `<class 'type'>`;
    __bases__ – inherent for classes; it’s a tuple and contains information about the base classes of a class;
    __dict__ – inherent for both classes and instances; contains a dictionary (or other type mapping object) of the object's attributes.
"""

print()

class Dog:
    pass

dog = Dog()
print('"dog" is an object of class named:', Dog.__name__)
print()
print('class "Dog" is an instance of:', Dog.__class__)
print('instance "dog" is an instance of:', dog.__class__)
print()
print('class "Dog" is  ', Dog.__bases__)
print()
print('class "Dog" attributes:', Dog.__dict__)
print('object "dog" attributes:', dog.__dict__)

print()

for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element)) # they achieve the same thing
    
print()

# type(__name__, __bases__, __dict__) -> dynamically creates a new class

Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

print()

# get more complex:

def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()

""" 
This way of creating classes, using the type function, is substantial for Python's way of creating classes using the class instruction:

    after the class instruction has been identified and the class body has been executed, the class = type(, , ) code is executed;
    the type is responsible for calling the __call__ method upon class instance creation; this method calls two other methods:
        __new__(), responsible for creating the class instance in the computer memory; this method is run before __init__();
        __init__(), responsible for object initialization.

Metaclasses usually implement these two methods (__init__, __new__), taking control of the procedure of creating and initializing a new class instance. Classes receive a new layer of logic.
"""

print('\n----------------\n')

class My_Meta(type): # derived from 'type' making it a meta-class
    def __new__(mcs, name, bases, dictionary): # role is to call __new__ from the base class
        # mcs = refers to the class, name = class name, bases = base classes, dictionary = class attributes
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta' # add a new attribute to the class
        return obj # return the class

class My_Object(metaclass=My_Meta):
    pass

# for key in My_Object.__dict__:
#     print(key, ':', My_Object.__dict__[key])
    
print('\n'.join([f'{key} : {My_Object.__dict__[key]}' for key in My_Object.__dict__]))

print('\n----------------\n')

# more complex example

def greetings(self): # default func metaclass will add to the class if not present in __dict__
    print('from metaclass: Just a greeting function, but it could be something more serious like a check sum')

class My_Meta(type):
    def __new__(mcs, name, bases, dictionary): # very similar style to the previous example, just tailor fit to add func to dict if not present
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
myobj1.greetings() # greetings not present until class is instantiated and the metaclass adds it - very cool
myobj2 = My_Class2()
myobj2.greetings()

""" 
As you can see, there is a greetings() function defined that greets everyone who interacts with it. 
In a real-life scenario, it could be a function that is obligatory for every class and is responsible 
for the consistency of object attributes; it could be a function returning a checksum for some of an 
attribute's values.
"""

print('\n----------------\n')

""" 
The concept of metaclasses looks hard at first glance, 
BUT if you’re responsible for API design or development, 
metaclasses are the magic that could help you in your work.

When you want to change your classes automatically, but decorators are not efficient, then metaclasses should help you.
"""