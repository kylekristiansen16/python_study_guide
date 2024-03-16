""" 
Your task is to write a code which has exactly the same conversation with the user and:
1 - defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class should be deducted from the above dialog — call it "reverse engineering" if you want)
2 - defines a class able to encode the Vehicle object into an equivalent JSON string;
3 - defines a class able to decode the JSON string into the newly created Vehicle object.

Of course, some basic data validity checks should be done, too. We're sure you're careful enough to protect your code from reckless users.
"""

import json

class Vehicle:
    
    def __init__(self, registration_number: str, year_of_production: int, passenger: str, mass: float, *args, **kwargs):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass
        
        if args:
            print(f"extraneous args: {args}")
        if kwargs:
            print(f"extraneous kwargs: {kwargs}")
    
# breakpoint()

class VehicleEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__ # return a dictionary of the object's attributes
        else:
            return super().default(self, w) # call the default method of the superclass for all other cases
        
# breakpoint()

class VehicleDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)
    

# workflow #1:
# get the data for a vehicle from the user
# create Vehicle
# encode Vehicle into JSON
# print json

print("workflow #1")
registration_number = input("Enter registration number: ")
year_of_production = int(input("Enter year of production: "))
is_passenger_car = input("Is passenger car? (y/n): ")
vehicle_mass = float(input("Enter vehicle mass: "))

vehicle = Vehicle(registration_number, year_of_production, is_passenger_car, vehicle_mass)

json_vehicle = json.dumps(vehicle, cls=VehicleEncoder)

print(vehicle)
print(json_vehicle)

print()

# workflow #2: 
# accept json string from user 
# decode json string into Vehicle object

print("workflow #2")
json_string = input("Enter json string for vehicle: ")

print()

decoded_vehicle = json.loads(json_string, cls=VehicleDecoder)

# {"passenger": "n", "registration_number": "35", "mass": 985.432, "year_of_production": 1995}

print(f"decoded vehicle: {decoded_vehicle}")
print(f"decoded vehicle dict {decoded_vehicle.__dict__}")