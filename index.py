""" import the python datetime module to help us create a timestamp"""
from animals import (
    Camel,
    Giraffe,
    Goat,
    Horse,
    Llama,
    Clownfish,
    Dolphin,
    Seal,
    Starfish,
    TigerFish,
    Copperhead,
    Gartersnake,
    Komodo,
    Monitorlizard,
    Rattlesnake,
)
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
whacky_wetlands = Wetlands("Whacky Wetlands")

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday", "llama chow", 12345)
miss_eyelashes = Camel("Miss Eyelashes", "Camel", "morning", "camel food", 12345)
horsey_mchorse = Horse("Horsey McHorseface", "Horse", "afternoon", "horse food", 12345)
goatty = Goat("Goatty McGoat", "Goat", "morning", "goat food", 12345)
necky = Giraffe("Necky", "Giraffe", "midday", "giraffe food", 12345)

varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(miss_eyelashes)
varmint_village.animals.append(horsey_mchorse)
varmint_village.animals.append(goatty)
varmint_village.animals.append(necky)

sssnakey = Rattlesnake("Sssnakey", "Rattlesnake", "snake food", 12345)
montey = Monitorlizard("Montey", "Monitor Lizard", "lizard food", 12345)
drogo = Komodo("Drogo", "Komodo Dragon", "dragon food", 12345)
cypress = Gartersnake("Cypress", "Garter Snake", "snake food", 12345)
copper = Copperhead("Copper", "Copperhead Snake", "snake food", 12345)

slither_inn.animals.append(sssnakey)
slither_inn.animals.append(montey)
slither_inn.animals.append(drogo)
slither_inn.animals.append(cypress)
slither_inn.animals.append(copper)

flipper = Dolphin("Flipper", "Dolphin", "dolphin food", 12345)
nemo = Clownfish("Nemo", "Clownfish", "fish food", 12345)
polaris = Starfish("Polaris", "Starfish", "starfish food", 12345)
tigger = TigerFish("Tigger", "Tigerfish", "fish food", 12345)
rose = Seal("Rose", "Seal", "seal food", 12345)

whacky_wetlands.animals.append(flipper)
whacky_wetlands.animals.append(nemo)
whacky_wetlands.animals.append(polaris)
whacky_wetlands.animals.append(tigger)
whacky_wetlands.animals.append(rose)

print(varmint_village)
print(slither_inn)
print(whacky_wetlands)

miss_fuzz.feed_llama()
miss_fuzz.feed()
