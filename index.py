""" import the python datetime module to help us create a timestamp"""
from datetime import date
from walking import Camel, Giraffe, Goat, Horse, Llama
from swimming import Clownfish, Dolphin, Seal, Starfish, TigerFish
from slithering import Copperhead, Gartersnake, Komodo, Monitorlizard, Rattlesnake
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
whacky_wetlands = Wetlands("Whacky Wetlands")

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday", "llama chow")
miss_eyelashes = Camel("Miss Eyelashes", "Camel", "morning", "camel food")
horsey_mchorse = Horse("Horsey McHorseface", "Horse", "afternoon", "horse food")
goatty = Goat("Goatty McGoat", "Goat", "morning", "goat food")
necky = Giraffe("Necky", "Giraffe", "midday", "giraffe food")

varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(miss_eyelashes)
varmint_village.animals.append(horsey_mchorse)
varmint_village.animals.append(goatty)
varmint_village.animals.append(necky)

sssnakey = Rattlesnake("Sssnakey", "Rattlesnake", "snake food")
montey = Monitorlizard("Montey", "Monitor Lizard", "lizard food")
drogo = Komodo("Drogo", "Komodo Dragon", "dragon food")
cypress = Gartersnake("Cypress", "Garter Snake", "snake food")
copper = Copperhead("Copper", "Copperhead Snake", "snake food")

slither_inn.animals.append(sssnakey)
slither_inn.animals.append(montey)
slither_inn.animals.append(drogo)
slither_inn.animals.append(cypress)
slither_inn.animals.append(copper)

flipper = Dolphin("Flipper", "Dolphin", "dolphin food")
nemo = Clownfish("Nemo", "Clownfish", "fish food")
polaris = Starfish("Polaris", "Starfish", "starfish food")
tigger = TigerFish("Tigger", "Tigerfish", "fish food")
rose = Seal("Rose", "Seal", "seal food")

whacky_wetlands.animals.append(flipper)
whacky_wetlands.animals.append(nemo)
whacky_wetlands.animals.append(polaris)
whacky_wetlands.animals.append(tigger)
whacky_wetlands.animals.append(rose)

print(varmint_village)
print(slither_inn)
print(whacky_wetlands)


