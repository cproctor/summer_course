# forest.py
# ---------
# by Chris Proctor

# The Forest class provides an environment for Animals to encounter each other.
# I do not expect you to fuly understand the code in this module; you will probably
# understand it about halfway. Note places where you have questions so we can talk 
# about them.

# If you are interested in how any of these imported functions or classes 
# works, you can search the Python documentation and learn about it. 
import logging
import sys
from time import sleep
from animal import Animal
from random import sample
from collections import Counter

# Adjusting some default settings for logging, so that it prints out
# log messages at the command line
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")


class Forest:
    "A forest is an environment for Animals"

    def __init__(self, day_length=None, log=None):
        """
        When creating a new Forest, a user can optionally pass in a log object, 
        which collects messages as a program is running. By using different kinds
        of logs, it is possible to print messages, hide them, save them in a file, 
        tweet them, etc... If you don't want anything special, well use the default
        log.
        """
        self.log = log or logging
        self.animals_list = []
        self.day_length = 2
        self.current_day = 0

    def run(self):
        """
        Create an endless loop causing animals to encounter each other.
        """
        self.log.info("A lovely day in the forest.")
        while True:
            self.log.info("Day {}. {}".format(self.current_day, self.status()))
            self.current_day += 1
            if len(self.animals_list) > 1:
                self.animal_encounter()
                if self.day_length is not None:
                    sleep(self.day_length)
                else:
                    raw_input("")
            else:
                self.log.info("Game over. {} is alone in the forest.".format(self.animals_list[0]))
                break

    def animal_encounter(self):
        animal_one, animal_two = self.select_animals()
        self.log.debug("  {} encounters {}...".format(animal_one, animal_two))
        result = animal_one.encounter(animal_two)
        self.log.info("  " + result['message'])
        if result['action'] == "die":
            self.remove_animal(animal_one)
        if result['action'] == "eat":
            self.remove_animal(animal_two) 
        if result['action'] == "mate":
            for child in result['children']:
                self.add_animal(child)

    def select_animals(self):
        "Chooses two animals to have an encounter, if possible. Otherwise, returns None"
        if len(self.animals_list) >= 2:
            return sample(self.animals_list, 2)

    def add_animal(self, animal):
        "Adds an animal to the forest"
        if not isinstance(animal, Animal):
            raise ValueError("Only animals can be added to the forest!")
        if animal in self.animals_list:
            raise ValueError("{} is already in the forest!".format(animal))
        self.animals_list.append(animal)
        self.log.debug("  {} joined the forest".format(animal))

    def remove_animal(self, animal):
        "Removes an animal from the forest"
        if animal in self.animals_list:
            self.animals_list.remove(animal)
            self.log.debug("  {} left the forest".format(animal))
        else:
            raise ValueError("{} is not in the forest".format(animal))

    def status(self):
        "Returns a status report showing how many animals are in the forest"
        animal_counts = Counter()
        for animal in self.animals_list:
            animal_counts[animal.species] += 1
        animal_count_strings = ["{} {}s".format(count, species) for 
                species, count in animal_counts.items()]
        return "The forest contains {}".format(", ".join(animal_count_strings))
        
