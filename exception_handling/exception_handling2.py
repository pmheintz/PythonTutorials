"""
Handling exceptions with finally and else
"""

def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0
        # c = 10

        d = (a + b) / c
        print(d)
    except:
        print("Exception found!")
        # raise is used to tell caller that an exception was thrown
        raise Exception("This is an exception")
    else:
        print("No exceptions so this \"else\" block runs.")
    finally:
        print("This \"finally\" block always executes")

try:
    exceptionHandling()
except:
    print("The method exceptionHandling() \"raised\" an exception that was handled")