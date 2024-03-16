""" 
no way around implementing abstract classes, even if they're not used
must at lease include with pass statement

an abstract class provides a means for API
"""

import abc

# @abc.abstractclass  # there is no such thing as this annotation, all you need is to inherit the ABC class
class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')
        
class RedField(BluePrint):
    def yellow(self):
        pass
    def hello(self):
        pass

gf = GreenField()
gf.hello()

# bp = BluePrint() # TypeError: Can't instantiate abstract class BluePrint with abstract methods hello

rf = RedField() # same as BluePrint(), abstract method not yet implemented

bp = BluePrint() 