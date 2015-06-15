How a Deck should work
----------------------

- A Deck can be initialized empty (`Deck()`), or with optional arguments:
    - `cards` can be a list of ints which will be converted into Cards
    - if `shuffle` is `True`, the cards will be shuffled immediately.
    - For example, this is a deck ready for a game: `Deck(cards=range(52), shuffle=True)`
- A Deck''s representation and string should look like this:
  
      &lt;Deck: [&lt;AS&gt;, &lt;10H&gt;, &lt;5C&gt;, &lt;6D&gt;]&gt;

  (Hint: once Cards have proper representations, `[<AS>, <10H>, <5C>, <6D>]`
  is just the representation of a list containing cards. If you don''t define
  a __str__ method, the __repr__ method is used as a default.)
- `deck.shuffle()` should shuffle the cards in the deck. (Hint: 
  [random.shuffle](https://docs.python.org/2/library/random.html#random.shuffle)
  might be helpful here.
- `deck.draw()` should return the last card in the deck. This card should no longer
  be in the deck. If there are no cards in the deck, return `None`.
- `deck.peek()` should return the last card in the deck, but should not remove it
  from the deck. (You can call `deck.peek()` over and over with the same result; 
  this is not true for `deck.draw()`)
- `deck.count()` returns the number of cards in the deck.
- `deck.empty()` returns `True` or `False`, depending on whether there are any 
  cards in the deck.
- `deck.add(card)` adds a card to the end of the deck.
- `deck.add_deck(other_deck)` draws the cards in the other deck, one by one, and
  adds them to the deck.



