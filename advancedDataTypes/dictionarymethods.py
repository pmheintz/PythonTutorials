"""
Dictionary methods
"""

car = {'make':'BMW', 'model':'550i', 'year':2016}
cars = {'bmw':{'model':'550i', 'year':2016}, 'benz':{'model':'E350', 'year':2015}}

print(car.keys())
print(cars.keys())
print(cars['benz'].keys())
print(car.values())
print(cars.values())
print(car.items())

print("*" * 20)
car_copy = car.copy()
print(car_copy)
# car.clear()
print(car.pop('model'))
print(car)