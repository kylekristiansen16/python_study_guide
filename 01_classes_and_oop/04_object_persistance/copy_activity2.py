
"""
The previous task was a very easy one. Now let's rework the code a bit:

introduce the Delicacy class to represent a generic delicacy. The objects of this class will replace the old school dictionaries. Suggested attribute names: name, price, weight;
your class should implement the __str__() method to represent each object state;
experiment with the copy.copy() and deepcopy.copy() methods to see the difference in how each method copies objects .
"""

class Delicacy:
    
    def __init__(self, name=None, price=None, weight=None) -> None:
        self.name = name
        self.price = price
        self.weight = weight
    
    def __str__(self) -> str:
        return f'{self.name} - {self.price} - {self.weight}'
    
licorice = Delicacy(name='Licorice',price=0.1,weight=251)
chocolate = Delicacy(name='Chocolate',price=1, weight=601)

import copy

print('licorice:', licorice)
print('chocolate:', chocolate)

print('\n')

licorice_2 = licorice # licorice_2 is a reference to licorice
chocolate_2 = chocolate

licorice_2.price = 0.2

print('licorice_2:', licorice_2, 'licorice_2 is licorice:', licorice_2 is licorice, 'licorice_2 == licorice:', licorice_2 == licorice, 'licorice_2 id:', id(licorice_2), 'licorice id:', id(licorice))
print('chocolate_2:', chocolate_2, 'chocolate_2 is chocolate:', chocolate_2 is chocolate, 'chocolate_2 == chocolate:', chocolate_2 == chocolate, 'chocolate_2 id:', id(chocolate_2), 'chocolate id:', id(chocolate))

print('\n')

licorice_copy = copy.copy(licorice) # licorice_copy is a copy of licorice, but it is not licorice
chocolate_copy = copy.copy(chocolate)

licorice_copy.price = 0.2

print('licorice_copy:', licorice_copy, 'licorice_copy is licorice:', licorice_copy is licorice, 'licorice_copy == licorice:', licorice_copy == licorice, 'licorice_copy id:', id(licorice_copy), 'licorice id:', id(licorice))
print('chocolate_copy:', chocolate_copy, 'chocolate_copy is chocolate:', chocolate_copy is chocolate, 'chocolate_copy == chocolate:', chocolate_copy == chocolate, 'chocolate_copy id:', id(chocolate_copy), 'chocolate id:', id(chocolate))

print('\n')

licorice_deepcopy = copy.deepcopy(licorice)
chocolate_deepcopy = copy.deepcopy(chocolate)

chocolate_deepcopy.weight = 783

print('licorice_deepcopy:', licorice_deepcopy, 'licorice_deepcopy is licorice:', licorice_deepcopy is licorice, 'licorice_deepcopy == licorice:', licorice_deepcopy == licorice, 'licorice_deepcopy id:', id(licorice_deepcopy), 'licorice id:', id(licorice))
print('chocolate_deepcopy:', chocolate_deepcopy, 'chocolate_deepcopy is chocolate:', chocolate_deepcopy is chocolate, 'chocolate_deepcopy == chocolate:', chocolate_deepcopy == chocolate, 'chocolate_deepcopy id:', id(chocolate_deepcopy), 'chocolate id:', id(chocolate))