# List Practice
# ----------------

This file contains some Python code that uses the various properties
of lists in Python. You should open a Python session in terminal and 
type all these commands, to make sure you are comfortable with how they
work.

    >>> people = ["J", "M", "S", "M", "C", "A"]
    >>> people
    ['J', 'M', 'S', 'M', 'C', 'A']
    >>> people.sort()
    >>> people
    ['A', 'C', 'J', 'M', 'M', 'S']
    >>> for person in people: 
    ...     print("Hello, {}".format(person))
    ... 
    Hello, A
    Hello, C
    Hello, J
    Hello, M
    Hello, M
    Hello, S
    >>> last_person = people.pop()
    >>> last_person
    'S'
    >>> people
    ['A', 'C', 'J', 'M', 'M']
    >>> people.pop()
    'M'
    >>> people
    ['A', 'C', 'J', 'M']
    >>> numbers = range(10)
    >>> for number in numbers:
    ...     print("I love the number {}".format(number))
    ... 
    I love the number 0
    I love the number 1
    I love the number 2
    I love the number 3
    I love the number 4
    I love the number 5
    I love the number 6
    I love the number 7
    I love the number 8
    I love the number 9
    >>> squares = [number * number for number in numbers]
    >>> squares
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> cubes = [number * number * number for number in range(10)]
    >>> cubes
    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    >>> greetings = [ "Hello there, {}".format(person) for person in people ]
    >>> greetings
    ['Hello there, A', 'Hello there, C', 'Hello there, J', 'Hello there, M']
    >>> 
    

