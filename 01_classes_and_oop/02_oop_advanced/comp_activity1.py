""" 
properties and setters to protect internal variables... 
used without any logic, they don't do anything special, but they get powerful when you add logic that controls what can be done with the vars
"""
class Tires:
    def __init__(self, size) -> None:
        self.size = size
        self.__pressure = 0
        
    def pump(self, amount):
        self.__pressure += amount
    
    def get_pressure(self):
        return self.__pressure
    
class CityTires(Tires):
    size = 15
    def __init__(self) -> None:
        super().__init__(CityTires.size)

class OffRoadTires(Tires):
    size = 18
    def __init__(self) -> None:
        super().__init__(OffRoadTires.size)

class Engine:
    def __init__(self, fuel_type) -> None:
        self.fuel_type = fuel_type
        self.__state = 'off'
        
    def start(self):
        print('starting engine')
        self.__state = 'on'

    def stop(self):
        print('stopping engine')
        self.__state = 'off'
        
    def get_state(self):
        return self.__state
    
class ElectricEngine(Engine):
    fuel_type = 'electricity'
    def __init__(self) -> None:
        super().__init__(ElectricEngine.fuel_type)

class PetrolEngine(Engine):
    fuel_type = 'petrol'
    def __init__(self) -> None:
        super().__init__(PetrolEngine.fuel_type)
    
class Vehicle:
    def __init__(self, vin, engine = None, tires = None) -> None:
        self.vin = vin
        self.__engine = engine
        self.__tires = tires
    
    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine):
        if engine in [ElectricEngine, PetrolEngine]:
            self.__engine = engine
        else:
            raise ValueError('invalid engine type')
    
    @property
    def tires(self):
        return self.__tires
    @tires.setter
    def tires(self, tires):
        self.__tires = tires
        
city_car = Vehicle('1234', ElectricEngine(), CityTires())
print(f'city car engine: {city_car.engine.fuel_type}')
print(f'city car tires: {city_car.tires.size}')
print(f'city car engine state: {city_car.engine.get_state()}')
city_car.engine.start()
print(f'city car engine start: {city_car.engine.get_state()}')

print()

off_road_car = Vehicle('1234', PetrolEngine(), OffRoadTires())
print(f'off_road car engine: {off_road_car.engine.fuel_type}')
print(f'off_road car tires: {off_road_car.tires.size}')
print(f'off_road car tire pressure: {off_road_car.tires.get_pressure()}')
off_road_car.tires.pump(4)
print(f'off_road car tire pressure: {off_road_car.tires.get_pressure()}')

print()

off_road_car.engine = "combustion"
print(f'off_road car engine: {off_road_car.engine}')