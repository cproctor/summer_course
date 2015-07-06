from player import Player
from deck import Deck

class WarGame:
    def __init__(self):
        self.turn = 0
        self.p1 = Player("Player 1")
        self.p2 = Player("Player 2")
        startingDeck = Deck(range(52))
        while not startingDeck.empty():
            self.p1.win_card(startingDeck.draw())
            self.p2.win_card(startingDeck.draw())
    
    def play_turn(self):
        self.turn += 1
        self.log_start_turn()
        p1Card = self.p1.draw_card()
        p2Card = self.p2.draw_card()

        if not (p1Card and p2Card):
            self.log("Game over!")
            return False

        if p1Card != p2Card:
            if p1Card > p2Card:
                self.p1.win_card(p1Card)
                self.p1.win_card(p2Card)
                self.log("  P1 {} wins agains P2 {}".format(p2Card, p1Card))
            elif p2Card > p1Card:
                self.p2.win_card(p1Card)
                self.p2.win_card(p2Card)
                self.log("  P2 {} wins agains P1 {}".format(p2Card, p1Card))
        else:
            self.war(p1Card, p2Card)

    def war(self, p1Card, p2Card):
        self.log("  WAR! P1 {} and P2 {}.".format(p1Card, p2Card))
        p1WarPile = Deck([p1Card.number])
        p2WarPile = Deck([p2Card.number])

        while p1WarPile.peek() == p2WarPile.peek():
            for i in range(3):
                if self.p1.has_cards():
                    card = self.p1.draw_card()
                    self.log("    P1 draws {}".format(card))
                    p1WarPile.add(card)
            for i in range(3):
                if self.p2.has_cards():
                    card = self.p2.draw_card()
                    self.log("    P2 draws {}".format(card))
                    p2WarPile.add(card)
            if p1WarPile.peek() == p2WarPile.peek():
                self.log(" STILL FIGHTING! P1 {} P2 {}".format(
                    p1WarPile.peek(), 
                    p2WarPile.peek()
                ))
        if p1WarPile.peek() > p2WarPile.peek():
            self.log("  P1 Wins the war! P1 {}, P2 {}".format(
                p1WarPile.peek(), 
                p2WarPile.peek()
            ))
            self.p1.win_deck(p1WarPile)
            self.p1.win_deck(p2WarPile)
        else:
            self.log("  P2 Wins the war! P1 {}, P2 {}".format(
                p1WarPile.peek(), 
                p2WarPile.peek()
            ))
            self.p2.win_deck(p1WarPile)
            self.p2.win_deck(p2WarPile)
        
    def game_over(self):
        return self.p1.cards() == 0 or self.p2.cards() == 0

    def log_start_turn(self):
        self.log("TURN {}: P1 has {} cards and P2 has {} cards".format(
            self.turn, self.p1.cards(), self.p2.cards()
        ))

    def log(self, message):
        print(message)
