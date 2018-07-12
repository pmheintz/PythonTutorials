"""
List data type stores more than 1 value in a variable
"""

cars = ["Mazda", "Nissan", "Honda"]
empty_list = []
print(cars)
print(empty_list)
print("*" * 20)

print(cars[0])

num_list = [1, 2, 3]
print(num_list)
sum_list = num_list[0] + num_list[1]

print(sum_list)

more_cars = ["Mazda", "Nissan", "Honda"]
print(more_cars[1])

more_cars[1] = "BMW"
print(more_cars[1])
print(more_cars)