
class Animal:

    """
    This class defines an animal. Animal should be subclassed for representations of 
    other animals.
    """

    def __init__(self, name, log):
        "When animals are created, they should be given "
        self.name = name
        self.log = log

    def validate(self):
        return True


    def encounter(self, other_animal):
        pass

class InvalidAnimalError(Exception):
    """
    Errors are objects too! Here, we have created a special error for when 
    an animal is not valid. We don't need any special behavior different from 
    the usual behavior of an Exception.
    """
