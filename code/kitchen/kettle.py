# kettle.py
# ---------
# by Chris Proctor
# This module defines a Kettle, an essential part of any tea party.
# This file doesn't do much on its own--it will be most useful 
# if you run it with python -i kettle.py, or if you import Kettle
# into another script.

class Kettle:

    water_level=10
    temp = "cold"

    # __repr__ is a magic method... It determines how Kettles are represented in Terminal.
    def __repr__(self):
        return "<Kettle with {} {} water>".format(self.water_level, self.temp)

    def boil(self):
        self.temp = "hot"
        if self.water_level > 0:
            self.water_level -= 1
        else:
            print("FIRE!!!")

    def throw(self, target):
        self.water_level = 0
        print("Hahaha! I just hit {}".format(target))

    def fill(self):
        self.water_level = 10

    def pour(self, amount):
        if amount <= self.water_level:
            self.water_level -= amount
            print("You poured out {} {} water!".format(amount, self.temp))
        else:
            print("Sorry, you could only pour out {} {} water.".format(self.water_level, amount))
            self.water_level = 0
        
        
kettle = Kettle()
print("OK, now there's a Kettle called kettle. Perhaps we should boil some water?")

    
