"""
Iterating multiple lists at the same time
"""

l1 = [1, 2, 3]
l2 = [6, 7, 8, 20, 30, 40]

# Zip iterates only as long as the shorter list
for a, b in zip(l1, l2):
    print(a)
    print(b)

