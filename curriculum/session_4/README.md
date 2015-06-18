Session 3
=========

Preparation
-----------

Try the [homework from session 2](https://github.com/cproctor/summer_course/tree/master/curriculum/session_2) and come to class with questions. You don't have to complete everything--stop if you get stuck!

Today's plan
------------

0. Questions about our coding. What's not working in card.py

    - The card specification says a `ValueError` should be raised if a card
      is initialized with anything other than an int between 0 and 51. 
      `ValueError` is a subclass of Exception, the object that represents an 
      error, mistake, or problem. You can `raise` an error to cause it to crash
      the program--it makes sense to do this if the code is being used improperly,
      so that the programmer can learn as quickly as possible that there's a 
      problem.

    - The `\_\_cmp\_\_` method gave several of us trouble. It should be defined 
      like this:
 
          def __cmp__(self, other_card):
         
      This method should return a positive int (like 1) if `self` is greater, 0 if
      the two cards are equal, and a negative int (like -1) if `other_card` is 
      greater.

1. We spent most of the class working on `deck.py`, which should match the
   specifications in `deck_specification.md`, and which should pass all the
   tests in `test_deck.py`. Based on the specification, we figured out that
   `deck.py` should start like this:

        
        # deck.py
        # -------
        # by Chris Proctor
        # this makes a deck of cards.
        
        from card import Card
        from random import shuffle
        
        class Deck:
        
            def __init__(self, cards=None, shuffle=False):
                if cards is None:
                    self.cards = []
                else:
                    # cards is something like [48, 49 50, 51]
                    # How do I turn ints into Cards?
                    self.cards = [ Card(number) for number in cards ]
        
            def __repr__(self):
                return "I'm a useless deck of cards."
        
            def shuffle(self):
                pass
        
            def draw(self):
                pass
        
            def peek(self):
                pass
        
            def count(self):
                pass
        
            def empty(self):
                pass
        
            def add_card(self, card):
                pass
        
            def add_deck(self, deck):
                pass
        
Homework
--------

See if you can complete `deck.py` so that it passes all the tests in 
test\_deck.py. If you get stuck, send Chris an email or stop and 
bring your questions to our next meeting. 
