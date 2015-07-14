from player import Player
from deck import Deck

class War:
    "A game of War."

    def __init__(self):
        """Sets up the players and the deck for a game of war. Then deals 
        out the cards to the players. Sets self.battles to 0. Finally, 
        creates a battle deck for each player. This will be used in the
        battle method."""
        self.battles = 0
        self.playerOne = Player()
        self.playerTwo = Player()
        self.battleDeckOne = Deck()
        self.battleDeckTwo = Deck()
        startingDeck = Deck(range(52), shuffle=True)
        while not startingDeck.empty():
            self.playerOne.take_card(startingDeck.draw())
            self.playerTwo.take_card(startingDeck.draw())

    def play(self):
        """Plays the entire game of war until it is over, then returns an
        int showing how many battles were in the game."""
        while not self.game_is_over():
            self.battle()
            self.battles += 1
        return self.battles

    def game_is_over(self):
        """Returns True if the game is over (if either player has no cards). 
        Otherwise returns False."""
        return not (
            self.playerOne.has_any_cards() and self.playerTwo.has_any_cards()
        )

    def battle(self):
        """ Plays a battle between the two players. There are a few steps:
            1. Draw cards for battle (try to draw a card for each player)
            2. If the top cards in each battle deck are different, then one 
               player has won the battle. Have the winning player take both
               decks.
            3. If the top cards in each battle deck are the same, then have
               each player draw three cards for battle, and then call battle
                again.
        """
        self.draw_cards_for_battle()
        if self.battleDeckOne.peek() == self.battleDeckTwo.peek():
            for _ in range(3):
                self.draw_cards_for_battle()
            self.battle()
        elif self.battleDeckOne.peek() > self.battleDeckTwo.peek(): 
            self.playerOne.take_deck(self.battleDeckOne)
            self.playerOne.take_deck(self.battleDeckTwo)
        else:
            self.playerTwo.take_deck(self.battleDeckOne)
            self.playerTwo.take_deck(self.battleDeckTwo)

    def draw_cards_for_battle(self):
        """Tries to draw a card from each player. If the player has a card, 
        adds it to the appropriate battle deck"""
        cardOne = self.playerOne.draw()
        if cardOne:
            self.battleDeckOne.add(cardOne)
        cardTwo = self.playerTwo.draw()
        if cardTwo:
            self.battleDeckTwo.add(cardTwo)
