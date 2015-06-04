# Animal.py
# ---------
# by Chris Proctor

# This module implements the class Animal, which represents an animal. 
# Animals are not very interesting on their own, but they can be subclassed
# to create your own, more interesting animals. You will need to understand
# the code in this module well, so ask if you have any questions about how
# something works.

class Animal:

    """
    This class defines an animal. Animal should be subclassed for representations of 
    other animals.
    """

    species = "animal"

    def __init__(self, name, traits=None):
        self.name = name

    def __str__(self):
        return "{} the animal".format(self.name)

    def __repr__(self):
        return "<animal named {}>".format(self.name)

    def encounter(self, other_animal):
        """
        Encounter should always return a dict representing the result of the encounter.
        This must include a message an an action. Supported actions include "die", "eat", 
        and "mate". If the action is "mate", then "children" should be a list containing
        zero or more Animals.
        """
        return {
            "message": "Hello there, {}".format(other_animal.name),
            "action": None, 
            "children": []
        }

    def mate(self, other_animal):
        """
        Mate should return a list containing zero or more Animals.
        """
        return [Animal("Child of {}".format(self.name))]
