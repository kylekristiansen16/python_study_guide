""" 
everything has a class
    class definitions -> metaclass
    class instances -> class
    functions/methods -> method
    variables -> datatype (int, float, str, list, dict, tuple, set, bool, etc.)
"""

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male") # instance of the class into variable object called duckling
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

drake.quack() # method attribute acces
print(duckling.height) # variable attribute access

print(f'Duck.__class__ : {Duck.__class__}') # class attribute access -> tells you the metaclass that it's derived from, same as type(Duck)
print(f'type(Duck) : {type(Duck)}') # class attribute access -> tells you the metaclass that it's derived from, same as Duck.__class__
print(duckling.__class__) # <class '__main__.Duck'> bc it's an instance of Duck in the __main__ scope
print(duckling.sex.__class__)
print(duckling.quack.__class__)
