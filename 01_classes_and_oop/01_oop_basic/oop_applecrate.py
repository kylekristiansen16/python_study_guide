"""  
feels like it's about how to use class variables to keep track of the number of instances of a class

"""

import random

class Apple:
    last_id = 0
    
    def __init__(self, weight):
        self.weight = weight
        
        Apple.last_id += 1
        self.id = f"a-{Apple.last_id}"

class AppleCrate:
    total_processed = 0
    total_weight = 0
    apples = []
    
    def add_apple(self, apple):
        AppleCrate.total_processed += 1
        AppleCrate.total_weight += apple.weight
        AppleCrate.apples.append(apple)

crate = AppleCrate()

constraints_met = True
while constraints_met:
    weight = random.uniform(0.2, 0.5)
    apple = Apple(weight)
    
    crate.add_apple(apple)
    
    if AppleCrate.total_weight > 300:
        constraints_met = False
    
    # print(AppleCrate.total_processed, AppleCrate.total_weight)
    

print(f"number of apples: {AppleCrate.total_processed}\ntotal weight of apples: {AppleCrate.total_weight}") # calling the class itself, not an instance of the class
print(f"apples in crate: {' '.join( [a.id for a in AppleCrate.apples[-5:]] )}")
print()
print(f"number of apples: {crate.total_processed}\ntotal weight of apples: {crate.total_weight}") # calling the instance of the class

    
    