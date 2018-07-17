# Base (parent) class
class Car(object):

    def __init__(self):
        print("You just created a Car instance.")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

# Derived (child) class
class BMW(Car):

    def __init__(self):
        # Base class is super, not required in this instance
        Car.__init__(self)
        # or...
        # super(BMW, self).__init__()
        print("You just created a BMW instance.")

c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()