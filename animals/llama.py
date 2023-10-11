from datetime import date
from .animal import Animal


class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def feed_llama(self):
        print(
            f'On {date.today().strftime("%m/%d/%Y")} {self.name} was fed {self.food} to the sounds of Simon and Garfunkle'
        )
