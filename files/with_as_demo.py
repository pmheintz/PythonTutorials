"""
With / As keywords
Helps with explicitly closing file without manually having to do it
"""

# print("Normal write start")
# myWrite = open("textfile.txt", "w")
# myWrite.write("Trying to write to the file")
# myWrite.close()
#
# print("Normal read start")
# myRead = open("textfile.txt", "r")
# print(str(myRead.read()))

# Using "with as" allows omitting the close()
print("With \"as\" write start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write")

print()
print("With \"as\" read start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))

