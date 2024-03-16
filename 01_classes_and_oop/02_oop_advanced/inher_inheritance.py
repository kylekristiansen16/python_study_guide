""" 
always remember the MRO (Method Resolution Order) - the order in which Python looks for a method in a hierarchy of classes
- diamond shaped, left to right
"""

class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

class E(C, B):
    pass

D().info() # class B bc B is resolved first
E().info() # class C bc C is resolved first - MRO order matters!

class Scanner:
    def scan(self):
        return'Scanner Scan'

class Printer:
    def print(self):
        return'Printer Print'

class Fax:
    def send(self):
        return 'Fax Send'
    
    def print(self):
        return 'Fax Print'
        
class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

print(f"mfd spf scan print send: {MFD_SPF().scan()}, {MFD_SPF().print()}, {MFD_SPF().send()}")
print(f"mfd spf scan print send: {MFD_SFP().scan()}, {MFD_SFP().print()}, {MFD_SFP().send()}")