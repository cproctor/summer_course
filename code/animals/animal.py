# animal.py
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
        "This magic method is called whenever an Animal is created"
        self.name = name

    def __str__(self):
        """
        This magic method provides the string representation for the Animal. 
        For example, this is what you get when you format the Animal into another string
        """
        return "{} the {}".format(self.name, self.species)

    def __repr__(self):
        """
        This magic method provides the representation you get when the Animal is shown 
        in the Terminal. For example, if you type Animal("Suzy"), you will see the result of
        this Method
        """
        return "<{} named {}>".format(self.species, self.name)

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
        child = Animal("Child of {}".format(self.name))
        return [child]
