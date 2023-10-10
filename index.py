""" import the python datetime module to help us create a timestamp"""
from datetime import date
from walking import Camel, Giraffe, Goat, Horse, Llama
from swimming import Clownfish, Dolphin, Seal, Starfish, TigerFish
from slithering import Copperhead, Gartersnake, Komodo, Monitorlizard, Rattlesnake


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday", "Llama chow")
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
miss_fuzz.feed()
miss_eyelashes = Camel("Miss Eyelashes", "Camel", "morning")
horsey_mchorse = Horse("Horsey McHorseface", "Horse", "afternoon")
goatty = Goat("Goatty McGoat", "Goat", "morning")
necky = Giraffe("Necky", "Giraffe", "midday")

flipper = Dolphin("Flipper", "Dolphin")
nemo = Clownfish("Nemo", "Clownfish")
polaris = Starfish("Polaris", "Starfish")
tigger = TigerFish("Tigger the Tigerfish", "Tigerfish")
rose = Seal("Rose", "Seal")

sssnakey = Rattlesnake("Sssnakey", "Rattlesnake")
montey = Monitorlizard("Montey", "Monitor Lizard")
drogo = Komodo("Drogo", "Komodo Dragon")
cypress = Gartersnake("Cypress", "Garter Snake")
copper = Copperhead("Copper", "Copperhead Snake")
