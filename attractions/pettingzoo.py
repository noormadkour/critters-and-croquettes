

class PettingZoo:
    def __init__(self, name):
        self.name = name
        self.description = "a place to pet cute and fuzzy critters"
        self.animals = list()

    def __str__(self):
        string = f"{self.name} is {self.description}, like: \n"
        for animal in self.animals:
            string += f"\t* {animal.name} the {animal.species}, who is available for petting at {animal.shift}\n"
        return string


