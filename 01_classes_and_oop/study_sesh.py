
""" 
so many questions on the shelve module

----

duck typing = giving the same name to methods that do different things, 
- WRONG built in protection against calling unknown methods, all exceptions are handled in the standard way
- a fancy term for the assumption that class objects own methods that are called

----

copying a list with [:] slice does not create an independent object

----

when constructing a subclass that overrides methods from the parent class, you still have access to the super class methods

----

inheritance is a concept that allows for modeling a tight relation betweeen super and sub classes,

----

instance variable is a kind of variable that existings inside an object

----

is a pickle file format constant amongst different releases of python? 
- no, it's not, so you can't rely on it for long term storage
- it depends on the version of python you're using
- possible answers... no, nobody's expected wide compatibility

----

what is an abstract class?
- a blueprint for other classes, must contain at least one abstract method

----

is it possible to create an instance of an abstract class?
- no, because this is not the role of abstract classes, they are blueprints for other classes

----

exception chain is a concept of handling exceptions raised by other exception handling code
- a way to persist details of an exception when translating it into another exception
- implicit exception chaining = when an exception is raised during other exception handling code, so the __context__ attribute is set
- explicit exception chaining = when an exception is raised explicitly, so the __cause__ attribute is set

----

encapsulation allows for controlling access to selected attributes

----

in python, a magic method is a method that is called automatically when a specific event occurs
- its name starts and ends with double underscores

"""