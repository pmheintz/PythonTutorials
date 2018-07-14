"""
Variable scope
"""

# a = 10 # Global scope
#
# def test_method(a):
#     print("Value of local var 'a': " + str(a))
#     a = 2
#     print("New value of local 'a': " + str(a))
#
# print("Value of global 'a': " + str(a))
# test_method(a)
# print("Value of global 'a' after test_method: " + str(a))

a = 10 # Global scope

def test_method():
    global a
    print("Value of var 'a' in method: " + str(a))
    a = 2
    print("New value of 'a' in method: " + str(a))

print("Value of global 'a': " + str(a))
test_method()
print("Value of global 'a' after test_method: " + str(a))