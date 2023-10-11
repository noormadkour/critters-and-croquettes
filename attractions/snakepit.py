class SnakePit:
    def __init__(self, name):
        self.name = name
        self.description = "a slippery space for special serpents"
        self.animals = list()

    def __str__(self):
        string = f"{self.name} is {self.description}, like: \n"
        for animal in self.animals:
            string += f"\t* {animal.name} the {animal.species}\n"
        return string
