class Demo:
    class_var = 'shared variable'
    def __init__(self, value):
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

d1.another_var = 'another variable in the object' # add another instance variable unknown to the class

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)

print(Demo.class_var)
print(Demo.__dict__)

d3 = Demo(300)
print(d3.class_var) # class variable can be accessed, but should not be set from the class instancea
print(d3.__dict__) # does not print the class variable