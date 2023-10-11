class Attraction:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        string = f"{self.name} is {self.description}, like ({len(self)} animals): \n"
        for animal in self.animals:
            string += f"\t* {animal.name} the {animal.species}\n"
        return string

    def __len__(self):
        return len(self.animals)
    
    @property
    def last_critter_added(self):
        return f"The last critter added to this attraction was {self.animals[-1].name} the {self.animals[-1].species}"