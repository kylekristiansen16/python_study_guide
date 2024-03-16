# syllabus:
- Classes, instances, attributes, methods, as well as working with class and instance data;
- shallow and deep operations;
- abstract classes, method overriding, static and class methods, special methods;
- inheritance, polymorphism, subclasses, and encapsulation;
- advanced exception handling techniques;
- the pickle and shelve modules;
- metaclasses.


## OOP
fundamental concepts: inheritance, polymorphism, encapsulation, and abstraction.

definitions:
- class — an idea, blueprint, or recipe for an instance;
- instance — an instantiation of the class; very often used interchangeably with the term 'object';
- object — Python's representation of data and methods; objects could be aggregates of instances;
- attribute — any object or class trait; could be a **variable or method**;
- method — a function built into a class that is executed on behalf of the class or object; some say that it’s a 'callable attribute';
- type — refers to the class that was used to instantiate the object.

to be discussed:
- creation and use of decorators;
- implementation of core syntax;
- class and static methods;
- abstract methods;
- comparison of inheritance and composition;
- attribute encapsulation;
- exception chaining;
- object persistence;
- metaprogramming.

### type 
- it is the foremost type that any class can be inherited from;
- as a result, if you’re looking for the type of class, then `type` is returned;
- **in all other cases, it refers to the class that was used to instantiate the object**; it’s a general term describing the type/kind of any object;
- it’s the name of a very handy Python function that returns the class information about the objects passed as arguments to that function;
- it returns a new type object when type() is called with three arguments; we'll talk about this in the 'metaclass' section.

### variables
instance variable = exists when and only when it is explicitly created and added to an object. This can be done during the object's initialization, performed by the __init__ method, or later at any moment of the object's life. Furthermore, any existing property can be removed at any time.

class variables can be used for
- fixed information like description, configuration, or identification values;
- mutable information like the number of instances created (if we add a code to increment the value of a designated variable every time we create a class instance)

## python core syntax
operators are symbols that represent combination of objects in a specific way
- operators like '+', '-', '*', '/', '%' and many others;
- operators like '==', '<', '>', '<=', 'in' and many others;
- indexing, slicing, subscripting;
- built-in functions like str(), len()
- reflexion – isinstance(), issubclass()

The name of each magic method is surrounded by double underscores. Dunders indicate that such methods are not called directly, but called in a process of expression evaluation, according to Python core syntax rules.

## inheritance / polymorphism
polymorphism is the provision of a single interface to objects of different types. In other words, it is the ability to create abstract methods from specific types in order to treat those types in a uniform way.
- Imagine that you have to print a string or an integer — it is more convenient when a function is called simply print, not print_string or print_integer.

Duck typing is a fancy name for the term describing an application of the duck test: "If it walks like a duck and it quacks like a duck, then it must be a duck", which determines whether an object can be used for a particular purpose. An object's suitability is determined by the presence of certain attributes, rather than by the type of the object itself.

polymorphism is used when different class objects share conceptually similar methods (but are not always inherited)
polymorphism leverages clarity and expressiveness of the application design and development;
when polymorphism is assumed, it is wise to handle exceptions that could pop up.

## decorators
A decorator is a very powerful and useful tool in Python, because it allows programmers to modify the behavior of a function, method, or class.

Decorators allow us to wrap another callable object in order to extend its behavior.

Decorators rely heavily on closures and *args and **kwargs.

Interesting note:

the idea of decorators was described in two documents – PEP 318 and PEP 3129. Don't be discouraged that the first PEP was prepared for Python 2, because what matters here is the idea, not the implementation in a specific Python.

## class & static methods

These alternative types of method should be understood as tool methods, extending our ability to use classes, not necessarily requiring the creation of class instances to use them.
As a result, our perception of the Python class concept is extended by two types of specialized methods.

comparison:
1. a class method requires 'cls' as the first parameter and a static method does not; 
2. a class method has the ability to access the state or methods of the class, and a static method does not;
3. a class method is decorated by '@classmethod' and a static method by '@staticmethod';
4. a class method can be used as an alternative way to create objects, and a static method is only a utility method.

# abstract classes
An abstract class should be considered a blueprint for other classes, a kind of contract between a class designer and a programmer:

- the class designer sets requirements regarding methods that must be implemented by just declaring them, but not defining them in detail. Such methods are called abstract methods.
- The programmer has to deliver all method definitions and the completeness would be validated by another, dedicated module. The programmer delivers the method definitions by overriding the method declarations received from the class designer.

why abstract classes?
- we want our code to be polymorphic, so all subclasses have to deliver a set of their own method implementations in order to call them by using common method names.

remember that it isn’t possible to instantiate an abstract class, and it needs subclasses to provide implementations for those abstract methods which are declared in the abstract classes

When we’re designing large functional units, in the form of classes, we should use an abstract class. When we want to provide common implemented functionality for all implementations of the class, we could also use an abstract class, because abstract classes partially allow us to implement classes by delivering concrete definitions for some of the methods, not only declarations.

This capability is especially useful in situations where your team or third-party is going to provide implementations, such as with plugins in an application, even after the main application development is finished.

# encapsulation
Encapsulation is used to hide the attributes inside a class like in a capsule, preventing unauthorized parties' direct access to them. Publicly accessible methods are provided in the class to access the values, and other objects call those methods to retrieve and modify the values within the object.

Python introduces the concept of properties that act like proxies to encapsulated attributes. 

So, while the washing machine is processing your laundry, you are not able to directly access the laundry. This is how attribute encapsulation works.

## composition vs. inheritance
inheritance models a tight relation between two classes: the base class and the derived class, called a subclass.

The result of this relation is a subclass class that inherits all methods and all properties of the base class, and allows a subclass to extend everything that has been inherited. By extending a base class, you are creating a more specialized class. Moreover, we say that these classes are tightly coupled.

Inheritance models what is called an is a relation.
Examples:
- a Laptop is a (specialized form of) Computer;
- a Square is a (specialized form of) Figure;
- a Hovercraft is a Vehicle.

The inheritance concept is a powerful one, but you should remember that with great power comes great responsibility. When you are reckless, then with the inheritance (especially multiple inheritances) you can create a huge, complex, and hierarchical structure of classes.

This hierarchy would be hard to understand, debug, and extend. This phenomenon is known as the class explosion problem, and is one of the antipatterns of programming.

Composition:
This concept models another kind of relation between objects; it models what is called a `has a` relation.

Examples:
- a Laptop has a network card;
- a Hovercraft has a specific engine.

Composition is the process of composing an object using other different objects. The objects used in the composition deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a more complicated structure.

inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
composition projects a class as a container (called a composite) able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior. It’s worth mentioning that blocks are loosely coupled with the composite, and those blocks could be exchanged any time, even during program runtime.

## inheriting from built in classes
Python gives you the ability to create a class that inherits properties from any Python built-in class in order to get a new class that can enrich the parent's attributes or methods. As a result, your newly-created class has the advantage of all of the well-known functionalities inherited from its parent or even parents and you can still access those attributes and methods.

In the following example, we’ll create an implementation of our own list class, which will only accept elements of the integer type. But, wait – why might you need such an object?

Imagine that you need to collect the serial numbers of sold tickets. Sound reasonable enough?

Your new class will be based on the Python list implementation and will also validate the type of elements that are about to be placed onto it.

Python allows you to subclass any built-in class such as a list, tuple, dictionary, and many others;
by subclassing the built-ins, you can easily adapt generics to provide more sophisticated features;
by subclassing the built-ins, you can modify only the parts (methods, attributes) that you intend to modify, while all remaining parts will behave as good old built-ins.

# exceptions
objects that represent errors which occur during the execution of a program that disrupts the normal flow of the program's instructions.

- short introduction to exceptions;
- review of the named attributes of exception objects;
- introduction to chained exceptions;
- analysis of the traceback object of each exception.

## copying using shallow and deep operations
- object: label vs. identity vs. value;
- the `id()` function and the `is` operand;
- shallow and deep copies of the objects.

