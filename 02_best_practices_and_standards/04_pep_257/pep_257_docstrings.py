""" DOCSTRINGS 
all public modules, functions, classes, and methods that are exported by a given module should have docstrings.

Non-public methods do not need to contain docstrings. However, it is recommended that you leave a comment right 
after the def line describing what the method actually does.

Docutils, a Python Dosctring Processing System

one-line docstrings – they are used for simple and short descriptions, and should fit on one line
multi-line docstrings – they are used for more difficult cases, and should consist of a summary line 
    followed by one blank line and a more elaborate description
    
a docstring should prescribe the code segment's effect, not describe it. 
In other words, it should take the form of an imperative 
    (e.g. "Do this", "Return that", "Compute this", "Convert that", etc.), not a description (e.g. "Does this", "Returns that", "Forms this", "Extends that", etc.). For example:

"""

def greeting(name):
    """Take a name and return its replicated form."""
    return name * 2

def king_creator(name="Greg", ordinal="I", country="Neverland"):
    """Create a king following the article title naming convention.
    
    Keyword arguments:
    :arg name: the king's name (default: Greg)
    :type name: str
    :arg ordinal: Roman ordinal number (default: I)
    :type ordinal: str
    :arg country: the country ruled (default: Neverland)
    :type country: str
    """
    if name == "Voldemort":
        return "Voldemort is a reserved name."

"""
script docstrings 
    (in the sense of stand-alone programs/single file executables) should document the script's function, command line syntax, environment variables, and files. The description should be balanced in a way that it helps new users understand the script's usage, as well as provide a quick reference to all the program's features for the more experienced user;
module docstrings
    should list the classes, exceptions, and functions exported by the module;
package docstrings
    (understood as the docstring of the package's __init__.py module) should list the modules and subpackages exported by the package;
docstrings for functions and class methods 
    should summarize their behavior and provide information about the arguments (including optional arguments), values, exceptions, restrictions, etc.
class docstrings
    should also summarize its behavior as well as document the public methods and instance variables. For example:
"""

class Vehicle:
    """A class to represent a Vehicle.
    
    Attributes:
    -----------
    vehicle_type: str
        The type of the vehicle, e.g. a car.
    id_number: int
        The vehicle identification number.
    is_autonomous: bool
        self-driving -> True, not self-driving -> False

    
    Methods:
    --------
    report_location(lon=45.00, lat=90.00)
        Print the vehicle id number and its current location.
        (default longitude=45.00, default latitude=90.00)
    """
    
    def __init__(self, vehicle_type, id_number, is_autonomous=True):
        """
        Parameters:
        -----------
        vehicle_type: str
            The type of the vehicle, e.g. a car.
        id_number: int
            The vehicle identification number.
        is_autonomous: bool, optional
            self-driving -> True (default), not self-driving -> False
        """
        
        self.vehicle_type = vehicle_type
        self.id_number = id_number
        self.is_autonomous = is_autonomous
    
    def report_location(self, id_number, lon=45.00, lat=90.00):
        """
        Print the vehicle id number and its current location.
        
        Parameters:
        -----------
        id_number: int
            The vehicle identification number.
        lon: float, optional
            The vehicle's current longitude (default is 45.00)
        lat: float, optional
            The vehicle's current latitude (default is 90.00)
        """

""" 
reStructuredText, and it's the official Python documentation standard explained and described in PEP 287
Vs
NumPy/SciPy docstrings format (for details, click here, which is a combination of the Google docstrings format and the reStructuredText format.

"""