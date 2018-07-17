"""
Exceptions are errors that should be handled so our programs execute properly
"""

def exceptionHandling():
    try:
        a = 10
        b = "A string"
        # b = 20
        c = 0

        d = (a + b) / c
        print(d)
    # If you know which exception(s) will be thrown
    # except ZeroDivisionError:
    #     print("Divide by zero error")
    # except TypeError:
    #     print("This is a type error")
    # Generic catch all exception block will catch all exceptions
    except:
        print("This method threw at least one unspecified exception!")

exceptionHandling()