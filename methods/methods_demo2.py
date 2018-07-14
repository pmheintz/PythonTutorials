"""
Working with more methods
Adding documentation
"""

def sum_nums(n1, n2):
    """
    Get the sum of 2 numbers
    :param n1: first number
    :param n2: second number
    :return: sum of n1 and n2
    """
    return n1 + n2

sum1 = sum_nums(1, 2)
print(sum1)
print(sum_nums(5, 7))

string_add = sum_nums("one", "two")
print(string_add)

print("*" * 20)

def isMetro(city):
    l = ["sfo", "nyc", "la"]

    if city in l:
        return True
    else:
        return False

x = isMetro("boston")
print(x)