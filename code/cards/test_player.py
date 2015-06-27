# test_player.py
# --------------
# by Chris Proctor

# This script tests your implementation of the Player class. 
# Here we use the built-in unittest library.

from player import Player
from deck import Deck
from card import Card
import unittest

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_has_any_cards(self):
        self.assertTrue(not self.player.has_any_cards())
        self.player.take_card(Card(0))
        self.assertTrue(self.player.has_any_cards())

    def test_take_card(self):
        card = Card(0)
        self.player.take_card(card)
        self.assertEqual(self.player.draw_card(), card)

    def test_take_deck(self):
        clubsDeck = Deck(range(0, 52, 4))
        self.player.take_deck(clubsDeck)
        self.assertTrue(clubsDeck.empty())

    def test_draw_card(self):
        twoClubs = Card(0)
        threeClubs = Card(4)
        self.player.take_card(twoClubs)
        self.assertEqual(self.player.draw_card(), twoClubs)
        self.assertIsNone(self.player.draw_card())
        self.player.take_card(threeClubs)
        self.assertEqual(self.player.draw_card(), threeClubs)

    def test_shuffle_discard_deck_into_draw_deck(self):
        self.player.take_deck(Deck(range(52)))
        newDeck = Deck()
        while self.player.has_any_cards():
            newDeck.add(self.player.draw_card())
        self.assertEqual(newDeck.count(), 52)

# This runs all the tests
unittest.main()
