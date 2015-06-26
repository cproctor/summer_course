
class Card:
    "A card represents a playing card"

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    short_suits = ["C", "D", "H", "S"]
    short_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, number):
        if isinstance(number, int) and number >= 0 and number < 52:
            self.number = number
        else: 
            raise ValueError("Cards must be initialized with an integer between 0 and 51.")

    def __repr__(self):
        return "<{}>".format(self.short_name())

    def __str__(self):
        return self.name()

    def __cmp__(self, other):
        
        if self.number // 4 > other.number // 4:
            return 1
        elif self.number // 4 < other.number // 4:
            return -1
        else: 
            return 0

    def name(self):
        return "{} of {}".format(self.rank(), self.suit())

    def short_name(self):
        return "{}{}".format(self.short_rank(), self.short_suit())
        
    def suit(self):
        return self.suits[self.number % 4]

    def short_suit(self):
        return self.short_suits[self.number % 4]

    def rank(self):
        return self.ranks[self.number // 4]

    def short_rank(self):
        return self.short_ranks[self.number // 4]

