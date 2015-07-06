from deck import Deck

class Player:
    """Represents a player in a card game. When the player
    draws cards, she will draw from her draw deck. When the draw deck runs
    out, the discard pile will be shuffled into the draw deck. 
    When the player takes cards, they will go into the discard deck."""

    def __init__(self, name="Player"):
        """Sets up the player's draw deck and discard deck. """
        self.name = name
        self.drawPile = Deck()
        self.discardPile = Deck()

    def has_any_cards(self):
        """returns True if the player has any cards in either the draw or 
        the discard deck. Otherwise returns False."""
        return not (self.drawPile.empty() or self.discardPile.empty())

    def take_card(self, card):
        "Adds the card to the discard deck"
        self.discardPile.add(card)

    def take_deck(self, deck):
        "Adds the deck to the discard pile"
        self.discardPile.add_deck(deck)

    def draw_card(self):
        """Draws (and returns) a card from the draw pile if possible. If not, 
        shuffles the discard pile into the draw pile. If there are still no
        cards, returns None."""
        if self.drawPile.empty():
            self.shuffle_in_discard_pile()
            if self.drawPile.empty():
                return None
        return self.drawPile.draw()

    def shuffle_discard_deck_into_draw_deck(self):
        """Adds the discard deck to the draw deck and then shuffles the draw
        deck. No return value"""
        self.drawPile.add_deck(self.discardPile)
        self.drawPile.shuffle()

        
