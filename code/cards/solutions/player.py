from deck import Deck

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.drawPile = Deck()
        self.discardPile = Deck()

    def __str__(self):
        return self.name

    def has_any_cards(self):
        return not (self.drawPile.empty() or self.discardPile.empty())

    def take_card(self, card):
        self.discardPile.add(card)

    def take_deck(self, deck):
        self.discardPile.add_deck(deck)

    def draw_card(self):
        if self.drawPile.empty():
            self.shuffle_in_discard_pile()
            if self.drawPile.empty():
                return None
        return self.drawPile.draw()

    def shuffle_discard_deck_into_draw_deck(self):
        self.drawPile.add_deck(self.discardPile)
        self.drawPile.shuffle()

        
