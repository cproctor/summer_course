# Dict Practice
# ----------------

This file contains some Python code that uses the various properties
of dicts in Python. You should open a Python session in terminal and 
type all these commands, to make sure you are comfortable with how they
work.

    >>> smoothie = {
    ...     "name": "smoothie",
    ...     "color": "pink",
    ...     "temperature": "cold",
    ...     "ingredients": ["mango", "banana", "yogurt", "lime", "strawberries"]
    ... }
    >>> 
    >>> smoothie
    {'name': 'smoothie', 'color': 'pink', 'temperature': 'cold', 'ingredients': ['mango', 'banana', 'yogurt', 'lime', 'strawberries']}
    >>> smoothie["color"]
    'pink'
    >>> smoothie["ingredients"]
    ['mango', 'banana', 'yogurt', 'lime', 'strawberries']
    >>> len(smoothie["ingredients"])
    5
    >>> cookie = {
    ...     "name": "cookie",
    ...     "color": "brown",
    ...     "temperature": "warm",
    ...     "ingredients": ["flour", "sugar", "chocolate", "egg", "butter", "baking powder"]
    ... }
    >>> boba = {
    ...     "name": "boba",
    ...     "color": "cream",
    ...     "temperature": "hot",
    ...     "ingredients": ["tea", "sugar", "tapioca balls", "barley", "water"]
    ... }
    >>> 
    >>> treats = [smoothie, cookie, boba]
    >>> treats
    [{'name': 'smoothie', 'color': 'pink', 'temperature': 'cold', 'ingredients': ['mango', 'banana', 'yogurt', 'lime', 'strawberries']}, {'name': 'cookie', 'color': 'brown', 'temperature': 'warm', 'ingredients': ['flour', 'sugar', 'chocolate', 'egg', 'butter', 'baking powder']}, {'name': 'boba', 'color': 'cream', 'temperature': 'hot', 'ingredients': ['tea', 'sugar', 'tapioca balls', 'barley', 'water']}]
    >>> for treat in treats: 
    ...     print("A {} is a {} {}-colored treat".format(treat["name"], treat["temperature"], treat["color"]))
    ... 
    A smoothie is a cold pink-colored treat
    A cookie is a warm brown-colored treat
    A boba is a hot cream-colored treat
    >>> 
    >>> for treat in treats:
    ...     print("If you want to make a {}, you will need: {}".format(treat["name"], ", ".join(treat["ingredients"])))
    ... 
    If you want to make a smoothie, you will need: mango, banana, yogurt, lime, strawberries
    If you want to make a cookie, you will need: flour, sugar, chocolate, egg, butter, baking powder
    If you want to make a boba, you will need: tea, sugar, tapioca balls, barley, water
    
