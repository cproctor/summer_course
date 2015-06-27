
class War:
    "A game of War."

    def __init__(self):
        """Sets up the players and the deck for a game of war. Then deals 
        out the cards to the players. Sets self.battles to 0. Finally, 
        creates a battle deck for each player. This will be used in the
        battle method."""

    def play(self):
        """Plays the entire game of war until it is over, then returns an
        int showing how many battles were in the game."""
            
    def game_is_over(self):
        """Returns True if the game is over (if either player has no cards). 
        Otherwise returns False."""
        
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

    def draw_cards_for_battle(self):
        """ Tries to draw one card from each player into that player's battle
        deck. If the player has no more cards, no card is drawn. """

        
