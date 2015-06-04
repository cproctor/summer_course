# test_duck.py
# ------------
# by Chris Proctor

# This file tests the Duck class, which you will have to create. Make sure duck.py 
# is in the same folder so it can be imported.

from duck import Duck
from animal import Animal

class Ogre(Animal):
    species = "ogre"

def expect(expectation, message):
    if not expectation: 
        raise Exception("A test failed: {}".format(message))

daffy = Duck("Daffy")
diffy = Duck("Diffy")
ogre = Ogre("Oggie")

duck_encounter = daffy.encounter(diffy)
ogre_encounter = daffy.encounter(ogre)

expect(daffy.name == "Daffy", "Daffy's name should be Daffy")
expect(daffy.species == "duck", "Daffy's species should be 'duck'")
expect("{}".format(daffy) == "Daffy the duck", 
        "Daffy's string representation should be 'Daffy the duck'")
expect(duck_encounter['action'] == None, 
        "Ducks should not have actions when they meet each other")
expect(duck_encounter['message'] == "Quack! Daffy sees Diffy!", 
        "The message is wrong for when Daffy meets Diffy")
expect(ogre_encounter['action'] == 'die', 
        "Ducks should die when they meet ogres.")

print("All tests passed! Your duck acts the way a duck should act.")


# This sure seems like a messy way to test out code. Do you think it would be 
# possible to represent an expectation about code with a class?
# (You might be interested in reading about Python's built-in unittest module.)

    
