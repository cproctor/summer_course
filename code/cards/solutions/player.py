from deck import Deck

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.drawPile = Deck()
        self.discardPile = Deck()

    def __str__(self):
        return self.name

    def cards(self):
        return self.drawPile.count() + self.discardPile.count()

    def has_cards(self):
        return self.cards() != 0

    def win_card(self, card):
        self.discardPile.add(card)

    def win_deck(self, deck):
        self.discardPile.add_deck(deck)

    def draw_card(self):
        if self.drawPile.count() == 0:
            self.shuffle_in_discard_pile()
        return self.drawPile.draw()

    def shuffle_in_discard_pile(self):
        self.drawPile.add_deck(self.discardPile)
        self.drawPile.shuffle()

        
