# Lexicon.py
# ----------
# by Chris Proctor
# 
# This file defines a Lexicon class, which uses a tree structure to store 
# words, and allows you to check whether something is a word, even when you 
# have lots of possible words (There's a commonly-used collecion of about 
# 173,000 words accepted as English). 

# The most basic way to use this would be as follows:
# >>> from lexicon import Lexicon
# >>> lex = Lexicon()
# >>> lex.load_words()
# >>> lex.is_a_word('astounding')
# True
# >>> lex.is_a_word('frabjous')
# True
# >>> lex.is_a_word('dumbledore')
# False
# >>> lex.find_words('post')
# ['post', 'pots', 'opts', 'spot', 'stop', 'tops']

# This class was written with the intent for students to read it and study 
# how it works. Please email Chris if you're having trouble understanding
# how something here works. 

# Ooh--fancy! Permutations takes a list (or something like a list, such as a
# string) and gives you back every possible arrangement. For example:
# >>> for permutation in permutations([1, 2, 3]):
# ...     print(permutation)
# ... 
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
from itertools import permutations


class LexiconNode:
    """A LexiconNode represents a letter in a word, so that we can build
    a tree of words. When you want to add a word to the tree, make sure 
    there's a path tracing out the letters of the word, and that the final
    node has the property is_end_of_word set to True. To check whether
    a string is a word in the Lexicon, try to trace the letters of the string.
    If you can't trace them, or if the last node has is_end_of_word set to 
    False, then it's not a word.
    """

    def __init__(self):
        """Each node keeps track of two things: Whether this is the end of
        a word, and options for letters that can follow this one."""
        self.next_letters = {}
        self.is_end_of_word = False

    def __repr__(self):
        """Shows a representation of the node. Not necessary, but useful if 
        you are looking around inside a word tree."""
        next_letters = ', '.join(sorted(self.next_letters.keys()))
        return "<LexiconNode is_end_of_word={}, next_letters: {}>".format(self.is_end_of_word, next_letters)

    def add_word(self, word):
        """Uses a recursive process to add a word to the tree. Each node takes
        care of some of the work, and then passes the rest off to another node.
            Step 1 (Am I done yet?): If the word is an empty string, then it ends
                here. All we need to do is to set self.is_end_of_word to True.
            Step 2 (Solve part of the problem): Peel off the first letter in 
                the word. Get (or create) the LexiconNode that corresponds to 
                that letter in self.next_letters.
            Step 3 (Call the function again with a simpler argument): Send the
                rest of the word to that LexiconNode.
        """
        if len(word) == 0:
            self.is_end_of_word = True
        else:
            first, rest = word[0], word[1:]
            next_letter = self.get_or_create_next_letter(first)
            next_letter.add_word(rest)

    def is_a_word(self, word):
        """ Follows a process much like adding a word to see if a word is in
        the Lexicon. 
            Step 1: If there's nothing left in the word, then it ends here. 
                Check whether self.is_end_of_word is true.
            Step 2: Peel off the first letter of the word, and try to get the 
                LexiconNode that corresponds to it. (If you get a KeyError, 
                that means there is no such node, so it's not a word.)
            Step 3: Pass the rest of the word to the next LexiconNode.
        """
        if len(word) == 0:
            return self.is_end_of_word
        try:
            first, rest = word[0], word[1:]
            return self.next_letters[first].is_a_word(rest)
        except KeyError:
            return False

    def get_or_create_next_letter(self, letter):
        """ 
            A helper function that tries to look up a LexiconNode in
            self.next_letters, using a letter as the key. If that LexiconNode
            does not yet exist, then we create it. Then return it.
        """
        if not letter in self.next_letters.keys():
            self.next_letters[letter] = LexiconNode()
        return self.next_letters[letter]


        
class Lexicon:
    """ A lexicon is a collection of words. In our case, we are going to use a
    lexicon to hold all the words in the English language, so that we can 
    easily look up whether a string is a word. The Lexicon class doesn't really 
    do much; all the hard work is done recursively by LexiconNodes.
    """

    def __init__(self):
        "Creates a LexiconNode to be the root for all the words."
        self.root = LexiconNode()

    def load_words(self, word_file_name='all_english_words.txt'):
        """Reads a text file containing words, one by one, and adds them to the 
        the Lexicon. A file called all_english_words.txt is provided, which 
        contains about 173,000 words accepted as English.
        """
        word_file = open(word_file_name)
        for word in word_file:
            self.root.add_word(word.lower().strip())

    def add_word(self, word):
        "Adds a word to the lexicon."
        self.root.add_word(word)

    def is_a_word(self, possible_word):
        """Checks whether a word is in the lexicon; returns True or False"""
        return self.root.is_a_word(possible_word.lower())

    def find_words(self, letters):
        """Given a bunch of letters, finds all the arrangements that form a 
        word. The strategy is simple: make every possible arrangement of the 
        letters, and then only keep the ones that are actually words."""
        possible_words = [''.join(combo) for combo in permutations(letters)]
        return filter(self.is_a_word, possible_words)
