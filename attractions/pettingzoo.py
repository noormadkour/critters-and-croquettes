from .attraction import Attraction
from movements import Walking

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        string = f"{self.name} is {self.description}, like ({len(self)} animals): \n"
        for animal in self.animals:
            string += f"\t* {animal.name} the {animal.species}, who is available for petting at {animal.shift}\n"
        return string

    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.name}")
        except AttributeError:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.name}")
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.name} attraction.')