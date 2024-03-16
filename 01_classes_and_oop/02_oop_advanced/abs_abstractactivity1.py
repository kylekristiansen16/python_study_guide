# this activity doesn't make any sense
# helpful explanation: https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way

from abc import ABC, abstractmethod

class Scanner(ABC):
    counter = 0
    
    def __init__(self) -> None:
        Scanner.counter += 1
        self.scanner_serial_number = f"serial-{Scanner.counter}" 
    
    def scan_document(self):
        print('doc has been scanned')
    
    @abstractmethod
    def get_scanner_status(self):
        pass
    
class Printer(ABC):
    counter = 0
    
    def __init__(self) -> None:
        Printer.counter += 1
        self.printer_serial_number = f"serial-{Printer.counter}" 
        
    def print_document(self):
        print('doc has been printed')
    
    @abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Printer, Scanner):
    max_res = 100
    
    def __init__(self) -> None:
        Printer.__init__(self)
        Scanner.__init__(self)
        
    def get_scanner_status(self):
        print(f'max resolution: {MFD1.max_res}')
        print(f'scanner serial number: {self.scanner_serial_number}')
    
    def get_printer_status(self):
        print(f'max resolution: {MFD1.max_res}')
        print(f'printer serial number: {self.printer_serial_number}')

cheap = MFD1()
cheap.get_printer_status()
cheap.get_scanner_status()
cheap.print_document()
cheap.scan_document()

# how to make parent classes cooperate when they are meant to be inherited together:

""" 
the kwargs get picked up into variable values if those parameters are defined in method that they're fed to...
if they're not defined, they stay as kwargs and can be subsequently forwarded to the next method
"""
class CoopFoo:
    def __init__(self, **kwargs):
        print(f'in CoopFoo : {kwargs}')
        super().__init__(**kwargs)  # forwards all unused arguments
        self.foo = 'foo'

class CoopBar:
    def __init__(self, bar, **kwargs):
        print(f'in CoopBar : {kwargs}')
        super().__init__(**kwargs)  # forwards all unused arguments
        self.bar = bar

class CoopFooBar(CoopFoo, CoopBar):
    def __init__(self, bar='bar'):
        super().__init__(bar=bar)  # pass all arguments on as keyword
                                   # arguments to avoid problems with
                                   # positional arguments and the order
                                   # of the parent classes
                                   
test_coop_foo_bar = CoopFooBar()