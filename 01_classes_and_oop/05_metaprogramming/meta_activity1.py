""" 
task:
    - Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
    - the system was created by a group of volunteers who worked with no clear “clean coding” rules;
    - the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;
    - your task is to prepare a metaclass that is responsible for:
        - equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
        - equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.

* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).

    - Your metaclass should be used to create a few distinct legacy classes;
    - create objects based on the classes;
    - list the class names that are instantiated by your metaclass.

"""

from datetime import datetime
import time
from pprint import pprint

def get_instantiation_time(self):
    return self.instantiation_time

def __str__(self):
    return f'working out {self.workout} at the {self.__class__.__name__}'

class New_Meta(type):
    classes_instantiated = []
    
    def __new__(cls, name, bases, dictionary):
        # equipping all newly instantiated classes with time stamps
        dictionary['instantiation_time'] = datetime.now()
        
        # equipping all newly instantiated classes with the get_instantiation_time() method
        dictionary['get_instantiation_time'] = get_instantiation_time
        
        # bonus 
        dictionary['workout'] = 'full body' if 'workout' not in dictionary else dictionary['workout']
        dictionary['__str__'] = __str__ if '__str__' not in dictionary else dictionary['__str__']
        
        # append the class name in the __new__ method
        __class__.classes_instantiated.append(name)
        
        # return the new class
        obj = super().__new__(cls, name, bases, dictionary)
        return obj
    
# metaclass should be used to create a few distinct legacy classes
class Gym(metaclass=New_Meta):
    pass

class YogaStudio(metaclass=New_Meta):
    workout='flexibility'
    
class Waterfront(metaclass=New_Meta):
    workout='cardio'
    
# create objects based on the classes
gym = Gym()
time.sleep(2)
yoga_studio = YogaStudio()
time.sleep(2)
waterfront = Waterfront()

for element in (gym, yoga_studio, waterfront):
    pprint(f'{element} at {element.get_instantiation_time()}') 