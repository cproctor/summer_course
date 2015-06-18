Session 4
=========

Preparation
-----------

Try the [homework from session 3](https://github.com/cproctor/summer_course/tree/master/curriculum/session_3) and come to class with questions. You don't have to complete everything--stop if you get stuck!

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

    - The `__cmp__` method gave several of us trouble. It should be defined 
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

0. See if you can complete `deck.py` so that it passes all the tests in 
   test\_deck.py. If you get stuck, send Chris an email or stop and 
   bring your questions to our next meeting. 

1. We are going to build a game of War, as described in the 
   [Wikipedia article](https://en.wikipedia.org/wiki/War_(card_game)).
   What other classes will be needed? Make a plan for the other classes
   we will need and write a specification for each, following the model
   of `card_specification.md` and `deck_specification.md`. A few notes
   on the rules of War:
     - When a player wins cards in a battle, they will go into a discard pile.
       When a player's deck runs out, she shuffles her discard pile and uses 
       this as her deck.
     - We will use the variation where in a battle, three cards are played
       face down, and then another card is turned up to determine the
       winner of the battle.
     - If a player runs out of cards during a battle, the final card is used 
       as the face-up card for the remainder of the battle.


