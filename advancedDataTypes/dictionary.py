"""
Data type that stores data in key:value pairs
Not sequenced, no indexing
"""

car = {'make':'BMW', 'model':'550i', 'year':2016}
print(car)

d = {}

print(car['model'])
year = car['year']
print(year)

print(d)
d['one'] = 1
d['two'] = 2

print(d)
sum_1 = d['two'] + 8
d['two'] = d['two'] + 7
print(sum_1)
print(d['two'])