"""
Tuple
Similar to a list but immutable (cannot change them)
"""

myList = [1, 2, 3]
print(myList)
myList[0] = 0
print(myList)

myTuple = (1, 2, 3, 1, 1)
print(myTuple)

print(myTuple[2])

print(myTuple[1:])

print(myTuple.index(3))

print(myTuple.count(1)) # Counts how many time argument appears in tuple

