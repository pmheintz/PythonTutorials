"""
Creating a dictionary and handling an exception with it
"""

def exceptionHandling():
    car = {'make': 'Nissan', 'model': 'Altima', 'year': '2008'}
    try:
        print(car['color'])
    except:
        print("Key error! The key you are attempting to access does not exist!")
        raise Exception("Exception raised to caller")
    finally:
        print("Method exited properly.")

try:
    exceptionHandling()
except:
    print("The method \"exceptionHandling\" threw an exception and was not able to execute properly.")