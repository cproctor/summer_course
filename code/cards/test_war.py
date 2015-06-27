# test_war.py
# ------------
# by Chris Proctor

# This script tests your implementation of the War class. 
# Here we use the built-in unittest library.

from war import War
import unittest

class TestWar(unittest.TestCase):

    def setUp(self):
        self.game = War()

    def test_play(self):
        self.assertIsInstance(self.game.play(), int)

    def test_game_is_over(self):
        self.assertFalse(self.game.game_is_over())
        self.game.play()
        self.assertTrue(self.game.game_is_over())

unittest.main()
