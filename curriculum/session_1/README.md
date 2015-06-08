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
        - make sure everyone can write and run Python files
    - Communication; make sure we have the right email addresses

1. Review a few important Python data structures and other tidbits

    - lists
    - string formatting

1. Introduce the concept of Object-Oriented Programming.

    - classes, instances, methods
        - A *class* is the idea of an object
        - An *instance* is an object itself. There can be many instances that
          share the same *class*
    - Python class syntax
    - a few magic methods
        - \_\_init\_\_
        - \_\_repr\_\_
    - Play with a few classes: TeaKettle and Animals in the Forest

Homework
--------

Don't spend more than three hours on this. If you want to spend less, spend less.
If you get stuck, feel free to email Chris, or just stop--I expect everyone to come
to our next meeting with questions. 

0. Write Chris an email:
    - How did today go? How did it feel? What did you like? What did you not like?
    - What should we change for next time? 

1. Look at `list_practice.md` (under code/python\_practice). Open up a Python 
   session in Terminal and type in all the code in this file. Don't copy/paste;
   it's important to actually copy it so you get used to the language.

2. Go into code/kitchen and run `kettle.py`. Add a few methods to Kettle to make 
   it more kettle-like. Test them out!

3. Go into code/animals and run `run_forest.py`. Try defining a few more subclasses
   of Animal and put them into a forest together. If you get stuck, don't worry--
   I'd like to spend the first part of class next time talking about your questions. 

If you want more challenge: Try to change `code/animals/duck.py` so that 
`code/animals/duck.py` is content. Here's what it means to be a duck:

- A Duck's species should be "duck"
- When a Duck named Daffy encounters another Duck named Diffy, , the returned 
  message should be "Quack! Daffy sees Diffy!"
- If a Duck encounters an Ogre, the returned action should be "die" because Ogres
  eat Ducks. 

Coming up
---------

Next time, we're going to start by showing off our fancy teakettles and our forests
full of animals, and talking about any questions you have. Then we'll design some 
more classes.
