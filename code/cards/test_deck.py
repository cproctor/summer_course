# test_deck.py
# ------------
# by Chris Proctor

# This script tests your implementation of the Deck class. 
# Here we use the built-in unittest library.

from deck import Deck
from card import Card
import unittest

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.emptyDeck = Deck()
        self.fullDeck = Deck(range(52))
        self.acesDeck = Deck([48, 49, 50, 51])

    def test_init(self):
        self.assertEqual(self.emptyDeck.count(), 0)
        self.assertEqual(self.fullDeck.count(),52)

    def test_init_can_shuffle(self):
        shuffledDeck = Deck(range(52), shuffle=True)
        self.assertNotInSameOrder(self.fullDeck, shuffledDeck)

    def test_repr(self):
        self.assertEqual(self.emptyDeck.__repr__(), "<Deck: []>")
        self.assertEqual(self.acesDeck.__repr__(), "<Deck: [<AC>, <AD>, <AH>, <AS>]>")

    # How to test whether the deck shuffled? Start with two identical decks, 
    # shuffle one, and then compare them card by card. It's technically possible
    # to shuffle a deck randomly and end up with the same order of cards, but
    # it's INCREDIBLY unlikely. (In fact, every time you randomly shuffle a
    # deck of cards, it's extremely likely that you have just created an order
    # which has never before been created in the history of all humans shuffling
    # cards. Wow.
    def test_shuffle(self):
        shuffledDeck = Deck(range(52))
        shuffledDeck.shuffle()
        self.assertNotInSameOrder(self.fullDeck, shuffledDeck)

    def test_draw(self):
        self.assertEqual(self.acesDeck.draw(), Card(51))
        self.assertEqual(self.acesDeck.count(), 3)

    def test_peek(self):
        self.assertEqual(self.acesDeck.peek(), Card(51))
        self.assertEqual(self.acesDeck.count(), 4)

    def test_count(self):
        self.assertEqual(self.emptyDeck.count(), 0)
        self.assertEqual(self.acesDeck.count(), 4)
        self.assertEqual(self.fullDeck.count(), 52)

    def test_empty(self):
        self.assertTrue(self.emptyDeck.empty())
        self.assertFalse(self.acesDeck.empty())

    def test_add(self):
        self.fullDeck.add(Card(0))
        self.assertEqual(self.fullDeck.count(), 53)

    def test_add_deck(self):
        self.fullDeck.add_deck(self.acesDeck)
        self.assertEqual(self.fullDeck.draw(), Card(51))
        self.assertEqual(self.fullDeck.draw(), Card(50))
        self.assertEqual(self.fullDeck.draw(), Card(49))
        self.assertEqual(self.fullDeck.draw(), Card(48))
        
    def assertNotInSameOrder(self, deck1, deck2):
        foundADifference = False
        while not deck1.empty():
            if deck1.draw() != deck2.draw():
                foundADifference = True
                break
        self.assertTrue(foundADifference)
                
# This runs all the tests
unittest.main()
