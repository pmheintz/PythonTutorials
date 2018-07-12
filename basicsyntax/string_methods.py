"""
Examples of string methods in python
"""

first = "nyc"[0]
city = "New Berlin"
print(first)
ft = city[4]
print(ft)

"""
len() - length
lower() - to lower
upper() - to upper
str() - convert to string
"""

print("*********")
print(city.lower())
print(city.upper())
print(len(city))
print(city + " " + str(42))

# Concatenation
print("Hello" + " " + city + "!")