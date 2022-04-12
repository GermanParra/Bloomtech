# Classes represent some entity
# Class to represent a vehicles

''' String describing the purpose of the code below'''
# Class names should be UpperCamelCase
#parent class is more generic
class Vehicle:
    # static attribute
    wheels = 4

    # Constructor - defines user supplied attibutes that we want to use in creating an object
    # 3 required attributes, two optional attibutes, and one static
    def __init__(self, make, model, color, year=2021, mileage=0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
    def honk(self):
        print('HOOOONK!!!!')

    def drive(self, miles_driven):
        print('VROOOOM!!!!')
        self.mileage = self.mileage + miles_driven

#Child class is more specific and inherits attributes and methods from parent class
class Car(Vehicle):
    # Constructor - defines user supplied attibutes that we want to use in creating an object
    # 3 required attributes, two optional attibutes, and one static
    def __init__(self, make, model, color, style, year=2021, mileage=0):
        super().__init__(make, model, color, year, mileage)
        # only need to add the attribute that is not being inherited
        self.style = style 

# detect if the file is being imported in a REPL or being run as a script
# this statement condition will only be true if the file is being run as a script

print('Running in a REPL or a script')

if __name__=="__main__":
    my_car = Car('toyota', 'camry', 'gray', 'sedan', 2007, 251000)
    print(my_car.style)
    print(my_car.mileage)
    print(my_car.honk())



    