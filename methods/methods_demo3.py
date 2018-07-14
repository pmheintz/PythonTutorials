"""
Working with positional/optional parameters
"""

# No method overloading, so...
# You can set default values for params if nothing is passed
def sum_nums(n1=2, n2=4):
    """
    Get the sum of 2 numbers
    :param n1: first number
    :param n2: second number
    :return: sum of n1 and n2
    """
    return n1 + n2

print(sum_nums())
print(sum_nums(4))
print(sum_nums(5, 5))
print(sum_nums(n2=8))
print(sum_nums(n2=6, n1=5))