# test_card.py
# ------------
# by Chris Proctor

# This script tests your implementation of the Card class. 
# Here we use the built-in unittest library.

from card import Card
import unittest

class TestCard(unittest.TestCase):

    def setUp(self):
        self.twoOfClubs = Card(0)
        self.queenOfSpades = Card(43)

    def test_initialize(self):
        self.assertRaises(ValueError, Card, 52)

    def test_card_rank(self):
        self.assertEqual(self.twoOfClubs.rank(), "2")
        self.assertEqual(self.queenOfSpades.rank(), "Queen")

    def test_card_short_rank(self):
        self.assertEqual(self.twoOfClubs.short_rank(), "2")
        self.assertEqual(self.queenOfSpades.short_rank(), "Q")

    def test_card_suit(self):
        self.assertEqual(self.twoOfClubs.suit(), "Clubs")
        self.assertEqual(self.queenOfSpades.suit(), "Spades")
        
    def test_card_short_suit(self):
        self.assertEqual(self.twoOfClubs.short_suit(), "C")
        self.assertEqual(self.queenOfSpades.short_suit(), "S")
        
    def test_card_name(self):
        self.assertEqual(self.twoOfClubs.name(), "2 of Clubs")
        self.assertEqual(self.queenOfSpades.name(), "Queen of Spades")

    def test_card_short_name(self):
        self.assertEqual(self.twoOfClubs.short_name(), "2C")
        self.assertEqual(self.queenOfSpades.short_name(), "QS")
        
    def test_card_str(self):
        self.assertEqual(self.twoOfClubs.__str__(), "2 of Clubs")
        self.assertEqual(self.queenOfSpades.__str__(), "Queen of Spades")

    def test_card_repr(self):
        self.assertEqual(self.twoOfClubs.__repr__(), "<2C>")
        self.assertEqual(self.queenOfSpades.__repr__(), "<QS>")

    def test_card_comparison(self):
        self.assertTrue(self.twoOfClubs < self.queenOfSpades)
        queenOfHearts = Card(42)
        self.assertTrue(self.queenOfSpades == queenOfHearts)

# This runs all the tests
unittest.main()




