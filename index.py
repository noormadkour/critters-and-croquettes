""" import the python datetime module to help us create a timestamp"""
from datetime import date
from walking import Camel, Giraffe, Goat, Horse, Llama


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama")


miss_eyelashes = Camel("Miss Eyelashes", "Camel")


horsey_mchorse = Horse("Horsey McHorseface", "Horse")


goatty = Goat("Goatty McGoat", "Goat")


necky = Giraffe("Necky", "Giraffe")





flipper = Dolphin("Flipper", "Dolphin")





nemo = Clownfish("Nemo", "Clownfish")


class Starfish:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


polaris = Starfish("Polaris", "Starfish")


class TigerFish:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


tigger = TigerFish("Tigger the Tigerfish", "Tigerfish")


class Seal:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


rose = Seal("Rose", "Seal")


class Rattlesnake:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


sssnakey = Rattlesnake("Sssnakey", "Rattlesnake")


class Monitorlizard:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


montey = Monitorlizard("Montey", "Monitor Lizard")


class Komodo:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


drogo = Komodo("Drogo", "Komodo Dragon")


class Gartersnake:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


cypress = Gartersnake("Cypress", "Garter Snake")


class Copperhead:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


copper = Copperhead("Copper", "Copperhead Snake")
