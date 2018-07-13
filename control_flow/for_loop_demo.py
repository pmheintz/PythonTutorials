"""
For loops
"""

# Strings for loop
my_string = "abcabc"
for c in my_string:
    if c == "a":
        print("A", end=" ")
    else:
        print(c, end=" ")

print("*" * 20)

# List for loop
cars = ["BMW", "Benz", "Honda"]

for car in cars:
    print(car)

nums = (1, 2, 3)

for n in nums:
    print(n * 10)

print("*" * 20)

# Dictionary for loop
dict = {"one": 1, "two": 2, "three": 3}

for key in dict:
    print(key + " : " + str(dict[key]))

print("*" * 20)

for key,value in dict.items():
    print(key)
    print(value)