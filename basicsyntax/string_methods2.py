"""
More python string methods
"""

# Replace method
a = "1abc2abc3abc4abc"
print(a)
print(a.replace('abc', 'ABC'))
print(a.replace('abc', 'ABC', 2))
print("************")
# Substring method
sub = a[1]
print(sub)
# select from (and including) index 1 through (but not including) index 6
sub = a[1:6]
print(sub)
# A third number is the number of steps
sub = a[1:6:3]
print(sub)
