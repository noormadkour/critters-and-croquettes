# The package syntax is what allows for these clean import statements
from .animal import Animal
from movements import Walking, Swimming

class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, shift, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        self.shift = shift
        # no more self.swimming = True

    def honk(self):
        print("The goose honks. A lot")

    def walk(self):
        print(f'{self} waddles rather than walks')

    def swim(self):
        print(f'{self} can swim like a muthafucka though')

    def __str__(self):
        return f'{self.name} the Goose'