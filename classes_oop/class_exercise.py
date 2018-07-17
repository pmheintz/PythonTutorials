"""
Exercise to practice Python classes
"""

class Fruit(object):
    """
    Parent class that defines a fruit
    """
    # Member variable
    shape = 'unknown'

    def __init__(self, type='undefined'):
        """
        Default constructor
        :param type: the type of fruit
        """
        self.type = type
        print("Fruit grabbed.")

    def nutrition(self):
        """
        Prints nutrition information
        :return: none
        """
        print("Fruit is good for you!")

    def fruit_shape(self):
        """
        Prints the shape member variable
        :return:
        """
        print("This fruit is a(n) " + self.shape + " shape.")

class Apple(Fruit):
    """
    Apple derived class
    """
    def __init__(self):
        """
        Constructor
        """
        super(Apple, self).__init__()
        self.type = 'apple'
        self.shape = 'round'

    def nutrition(self):
        """
        Prints different nutrition information
        :return: none
        """
        print("An apple a day keeps the doctor away.")

    def color(self):
        """
        Prints the fruit color
        :return: none
        """
        print("This fruit is red.")

# Unit tests
my_fruit = Fruit()
print("This fruit is: " + my_fruit.type)
my_fruit.nutrition()
my_fruit.fruit_shape()
print("*" * 40)
my_apple = Apple()
print("This fruit is: " + my_apple.type)
my_apple.nutrition()
my_apple.fruit_shape()
my_apple.color()
