Session 2
=========

Preparation
-----------

Please try the [homework from session 1](https://github.com/cproctor/summer_course/tree/master/curriculum/session_1) and come to our meeting ready to share anything you've created (crazy tea kettles and forests!) I'm also looking forward to discussing any questions or places you got stuck--it would be especially good if you were able to show us some code that's not working, or that raised a question in your mind. No matter what you've been able to do, don't worry! It will be fine. 

It would be great if you could bring a laptop computer with you; I have extra if you'd like to borrow one.

Today's plan
------------

0. Share our work
    - We will start by sharing the code we have written for tea kettles and forests
    - Discuss your questions
    - Designing a duck

1. Back to Git
    - We will commit our work into our git repositories.

2. Practice with Python dicts
    - when to use a dict
    - aside: JSON, and saving data in files

3. A few magic methods
    - \_\_init\_\_ is called when a new instance of your class is created
    - \_\_str\_\_ defines the string representation of your class (how users should see it)
    - \_\_repr\_\_ defines how your class should appear when debugging
    - \_\_cmp\_\_ compares an instance with another instance. Should return a
      positive int if this instance is greater, 0 if the two are equal, and a
      negative int if the other instance is greater.

4. Start designing a card game

Homework
--------

0. Look at `code/python\_practice/dict\_practice.py. Open up Python in 
   Terminal and type all these commands so that you get some practice 
   with using dicts.

1. Write duck.py, which should define a subclass of Animal called Duck.
   When you run test_duck.py, it tests your version of Duck. Change Duck 
   until it passes all the tests.

2. Write a Card class to represent a playing card. Card should pass the 
   tests in test\_card.py. You can use card.py to get started. (Make sure 
   your card.py file stays in the same folder as test\_card.py, so that 
   the tests can find the code they're testing.)

4. Challenge: Start working on a Deck class to represent a pile of cards. Deck should
  pass the tests in test\_deck.py. You are not expected to complete Deck--
  work until you get stuck, come to Session 3 with questions.

Hint:

Here's some Python code that might be really helpful in converting integers between 
0 and 51 into the corresponding cards. It relies on integer division 
(which throws away the remainder) and mod (the opposite--throws away the answer to the
division problem and only keeps the remainder). 

    >>> suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    >>> ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    >>> for num in range(52):
    ...     rank = num / 4
    ...     suit = num % 4
    ...     print("The {} of {}".format(ranks[rank], suits[suit]))
    ... 
    The 2 of Clubs
    The 2 of Diamonds
    The 2 of Hearts
    The 2 of Spades
    The 3 of Clubs
    The 3 of Diamonds
    The 3 of Hearts
    The 3 of Spades
    The 4 of Clubs
    The 4 of Diamonds
    The 4 of Hearts
    The 4 of Spades
    The 5 of Clubs
    The 5 of Diamonds
    The 5 of Hearts
    The 5 of Spades
    The 6 of Clubs
    The 6 of Diamonds
    The 6 of Hearts
    The 6 of Spades
    The 7 of Clubs
    The 7 of Diamonds
    The 7 of Hearts
    The 7 of Spades
    The 8 of Clubs
    The 8 of Diamonds
    The 8 of Hearts
    The 8 of Spades
    The 9 of Clubs
    The 9 of Diamonds
    The 9 of Hearts
    The 9 of Spades
    The 10 of Clubs
    The 10 of Diamonds
    The 10 of Hearts
    The 10 of Spades
    The Jack of Clubs
    The Jack of Diamonds
    The Jack of Hearts
    The Jack of Spades
    The Queen of Clubs
    The Queen of Diamonds
    The Queen of Hearts
    The Queen of Spades
    The King of Clubs
    The King of Diamonds
    The King of Hearts
    The King of Spades
    The Ace of Clubs
    The Ace of Diamonds
    The Ace of Hearts
    The Ace of Spades
    >>> 
