# goat.py
# ---------
# by Chris Proctor

# This module implements the harmless goat. Who wouldn't want a few goats in their Forest?

from animal import Animal
from random import randint, choice

class Goat(Animal):
    
    goat_names = ["Goatee", "GoatGoat", "GoGoGoat", "Little Goat", "Big Goat"]
    
    species = "goat"

    def encounter(self, other_animal):
        if other_animal.species == 'goat':
            children = self.mate(other_animal)
            return {
                "message": "{} met {} and had {} children!".format(self, other_animal, len(children)),
                "action": "mate",
                "children": children
            }
        else:
            return {
                "message": "Baa! Hello, {}, I am {}!".format(other_animal, self),
                "action": None,
                "children": []
            }
            
    def mate(self, other_animal):
        number_of_offspring = randint(0, 5)
        children = [Goat(choice(self.goat_names)) for number in range(number_of_offspring)]
        return children
        
        
