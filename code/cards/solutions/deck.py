from card import Card
from random import shuffle

class Deck:
    "A deck represents a pile of cards"

    def __init__(self, cards=None, shuffle=False):
        if cards:
            self.cards = [Card(number) for number in cards]
        else:
            self.cards = []
        if shuffle:
            self.shuffle()

    def __repr__(self):
        return "<Deck: {}>".format(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        if any(self.cards):
            return self.cards.pop()
        else: 
            return None

    def peek(self):
        return self.cards[-1]

    def count(self):
        return len(self.cards)

    def empty(self):
        return self.count() == 0

    def add(self, card):
        if not isinstance(card, Card):
            print(card)
            raise ValueError("Only cards can be added to decks")
        self.cards.append(card)

    def add_deck(self, deck_to_add):
        card = deck_to_add.draw()
        while card is not None:
            self.add(card)
            card = deck_to_add.draw()
