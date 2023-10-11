from .attraction import Attraction

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        string = f"{self.name} is {self.description}, like ({len(self)} animals): \n"
        for animal in self.animals:
            string += f"\t* {animal.name} the {animal.species}, who is available for petting at {animal.shift}\n"
        return string
