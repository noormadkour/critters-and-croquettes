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

    @property
    def last_critter_added(self):
        return f"The last critter added to this attraction was {self.animals[-1].name} the {self.animals[-1].species}"
