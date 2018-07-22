"""
File I/O
Reading a file -> .read()
Reading line by line -> .readline()
"""

myFile = open("secondfile.txt", "r")

print(str(myFile.read()))
myFile.close()

print("Line by line =============>>")

myFileLine = open("secondfile.txt", "r")
print(str(myFileLine.readline()))
myFileLine.readline()
print(str(myFileLine.readline()))
myFileLine.close()