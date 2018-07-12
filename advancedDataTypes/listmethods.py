"""
Built in methods for manipulating lists
"""

cars = ["BMW", "Honda", "Audi"]

length = len(cars)
print(length)

cars.append("Mazda")
print(cars)

cars.insert(1, "Nissan")
print(cars)

x = cars.index("Honda")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("Nissan")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)
print("*" * 20)
cars.sort()
print(cars)