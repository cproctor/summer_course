# run_forest.py
# -------------
# by Chris Proctor

# This module is just a short script setting up a forest with a few boring
# animals. If you run this, the animals will chat with each other.

from forest import Forest
from animal import Animal

forest = Forest()
for name in ["Lily", "Todd", "Fred", "Suzanne"]:
    animal = Animal(name)
    forest.add_animal(animal)

forest.run()
    
