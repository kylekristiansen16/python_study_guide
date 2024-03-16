class Car:
    def __init__(self, engine):
        self.engine = engine

class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))

class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()

# In fact, with the composition approach you can more easily respond to the requirement changes regarding classes, 
# as it does not require deep dependency investigations which you would spot while implementing code with the inheritance approach.

# On the other hand, there is a clear drawback: composition transfers additional responsibilities to the developer. 
# The developer should assure that all component classes that are used to build the composite should implement the methods named 
# in the same manner to provide a common interface.

# You should always examine the problem your code is about to solve before you start coding. 
# If the problem can be modeled using an “is a” relation, then the inheritance approach should be implemented.

""" 
metaclasses would help with the composition because you could write them to guarantee certain methods are implemented
so that a class can be used to compose another with assurance that it meets the requirements
"""

### example 2

class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number

class Personal_Computer(Base_Computer):
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')

class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))

class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialling the access number ... '.ljust(40), end='')
        super().download()

class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem  ... '.ljust(40), end='')
        super().download()

class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()

# I started my IT adventure with an old-school dial up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download() # calling a method off the connection class instance inside the my_computer instance of Personal_Computer

# then it came year 1999 with ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()
