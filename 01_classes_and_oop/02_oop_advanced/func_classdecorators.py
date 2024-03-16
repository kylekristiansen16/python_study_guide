
def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__ # copy the original __getattribute__ method for storage

    def new_getattr(self, name): # define a new __getattribute__ method which logs the attribute access -> adds a print statement ahead of the original __getattribute__ method
        if name == 'mileage':
            print('IN NEW GETATTR: We noticed that the mileage attribute was read')
        return class_.__getattr__orig(self, name) # call the original __getattribute__ method after additional work is performed

    class_.__getattribute__ = new_getattr # replace the original __getattribute__ method with our new one
    return class_

@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage) # __getattribute__ is called when accessing the attribute
print('The VIN is', car.VIN)
