How a Card should work
----------------------

- A Card is initialized with an int between 0 and 51. Each int represents a 
  different card in a deck. `Card(0)` will be the 2 of Clubs and `Card(51)` will 
  be the Ace of Spades.The order goes like this:

  2 of Clubs, 2 of Diamonds, 2 of Hearts, 2 of Spades, 3 of Clubs, ... , 
  Ace of Hearts, Ace of Spades

  If a card is initialized with anything other than an int between 0 and 51, 
  a `ValueError` should be raised.

- `card.rank()` should return the appropriate element of Card.ranks 
- `card.short_rank()` should return the appropriate element of Card.short_ranks 
- `card.suit()` should return the appropriate element of Card.suits
- `card.short_suit()` should return the appropriate element of Card.short_suits 
- `card.name()` should return "2 of Clubs", "Jack of Diamonds", etc.
- `card.short_name()` should return "2C", "JD", etc.
- a card's string (the result of the `__str__` method being called)
  should be the same as `card.name()`
- a card's representation (the result of the `__repr__` method being called) should 
  be "<2C>", "<10D>", etc.
- You should be able to compare cards by rank. The 10 of Hearts is greater than
  the 5 of Spades; the 6 of Diamonds is equal to the 6 of Hearts. To do this you will
  need to add a \_\_cmp\_\_ method to Card which takes one argument--another card. 
  When you compare cards (like `card1 > card2`), what really happens is 
  card1.__cmp__(card2). \_\_cmp\_\_ should return an integer. If the first 
  number is greater, the integer should be greater than 0. If the two are 
  equal, return 0. And if the first number is less than the second number, 
  return an integer less than 0.
