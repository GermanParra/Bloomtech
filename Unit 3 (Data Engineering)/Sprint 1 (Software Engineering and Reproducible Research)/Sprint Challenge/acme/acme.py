
import numpy as np

#'''Describe code below here'''

class Product:
    '''Main Class decribing all acme products'''

    def __init__(self, name, price = 10, weight = 20, flammability = 0.5, identifier = 'None'):

        identifier = np.random.randint(1000000,10000000)

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        ''' calculates the price divided by the weight, and then returns a message:
            * if the ratio is less than 0.5 return "Not so stealable..."
            * if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable."
            * otherwise return "Very stealable!"'''
        if (self.price / self.weight) < 0.5:
            result = 'is a not so stealable product!'
            return result
        elif (self.price / self.weight) < 1:
            result = 'is kinda stealable!'
            return result
        else:
            result = 'is a very stealable product!'
            return result
    
    def explode(self):
        '''calculates the flammability times the weight, and then returns a message:
            * If the product is less than 10 return "...fizzle."
            * If it is greater or equal to 10 but less than 50 return "...boom!"
            * Otherwise return "...BABOOM!!"'''
        if (self.flammability * self.weight) < 10:
            result = '...fizzle.'
            return result
        elif (self.flammability * self.weight) < 50:
            result = '...boom!'
            return result
        else:
            result = '...BABOOM!!'
            return result


class BoxingGlove(Product):
    '''Subclass of `Product` to specifically decribing the Boxing Glove Product'''
    def __init__(self, name, price = 10, weight = 10, flammability = 0.5, identifier = 'None'):
        super().__init__(name, price, flammability, identifier)
        self.weight = weight

    def explode(self):
        '''Override the `explode` method from main class (Product)
             to always return "...it's a glove."'''
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif self.weight < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')
        
