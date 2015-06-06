# tiger.py
# ---------
# by Chris Proctor

# This module implements the fearsome Tiger, which eats everything it sees.

from animal import Animal

class Tiger(Animal):

    species = "tiger"

    def encounter(self, other_animal):
        return {
            "message": "Poor {} was eaten by {}".format(other_animal, self),
            "action": "eat",
            "children": None
        }
        

