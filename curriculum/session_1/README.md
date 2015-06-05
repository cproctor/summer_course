Session 1
=========

Preparation
-----------

We are going to be using git to share our work in this course. To get ready for
the first session, please do the following: 

1. Make an account on github.com. (By default, your code will be public, so don't 
use your real name. Many programmers today use their GitHub accounts as 
portfolios when they apply for jobs, so it's good to have it public. If you don't 
want your code to be public, you can get the 
[Student Developer Pack](https://education.github.com/pack/join), which gives you 
free private repositories.)

2. If you're not reading this in a web browser, go to the 
   [GitHub page for this project](https://github.com/cproctor/summer_course), 
   make sure you're logged in, and click "Fork" in the top right corner. This 
   will create your own copy of the course project. You will save your work in this 
   project, and will also see all the curriculum as Chris adds it from week to week.

3. Download [GitHub for Mac](https://mac.github.com/) or 
   [GitHub for Windows](https://windows.github.com/) as appropriate. Log in with 
   your GitHub username and password.

4. In the GitHub program, click "Sync" in the top right corner. You should see your
   copy of the Summer Course project appear. 

If you get stuck, don't worry. We'll straighten it all out when we meet in person.

Today's plan
------------

0. Course goals and norms.

    - Set up computers
    - Communication; make sure we have the right email addresses

1. Review a few important Python data structures and other tidbits

    - lists
    - dicts
    - functions
    - odds and ends
        - string formatting
        - documentation (docstrings and comments)

1. Introduce the concept of Object-Oriented Programming.

    - classes, instances, methods, interfaces, variable scope
    - Python class syntax
    - a few magic methods
        - __init__
        - __str__
        - __repr__
        - __cmp__
    - Play with a few classes: Animals in the Forest
    - Design classes for a card game.

Homework
--------

You should work on this for about three hours between now and Session 2. 

0. Implement a few other subclasses of Animal and update `run_forest.py`
   so that it lets them interact. See if you can create a dynamic but 
   stable ecosystem where predators keep other populations in check.

1. Write a Card class to represent a playing card. Card should pass the 
   tests in test_card.py. You can use card.py to get started. (Make sure 
   your card.py file stays in the same folder as test_card.py, so that 
   the tests can find the code they're testing.)

2. Start working on a Deck class to represent a pile of cards. Deck should
   pass the tests in test_deck.py. You are not expected to complete Deck--
   work until you get stuck, come to Session 2 with questions.


Coming up
---------

In the next few meetings we will be finishing the Card and Deck classes so that
we can write programs that play card games. Remember "war", that really boring 
card game you used to play when you were a kid? I've always wondered how long, 
on average, it takes to finish a game. We're going to find out!

By then we will be pretty comfortable desigining object-oriented solutions in 
Python, and we will be ready to start learning Java. (Coming from Python, Java 
might seem similar but just more irritating. We will be ready to understand why
some of Java's differences might actually be better.)

