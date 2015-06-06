# run__hobbesian_forest.py
# ------------------------
# by Chris Proctor

# "Life is nasty, brutish, short, and FULL of goats"
#                       - with apologies to Thomas Hobbes

from forest import Forest
from goat import Goat
from tiger import Tiger

forest = Forest()
for name in ["Greg", "Glenda", "Gaby"]:
    goat = Goat(name)
    forest.add_animal(goat)
for name in ["Tina", "Tigger", "Teeth"]:
    tiger = Tiger(name)
    forest.add_animal(tiger)

forest.run()
    

