"""
File I/O
'w'  -> write only mode
'r'  -> read only mode
'r+' -> read and write mode
'a'  -> append mode
"""

myList = [1, 2, 3]
myOtherList = ["first line", "second line", "third line"]

myFile = open("firstfile.txt", "w")

for item in myList:
    # Write requires strings, so casting is needed
    myFile.write(str(item) + "\n")

myFile.close()

myOtherFile = open("secondfile.txt", "w")

for stuff in myOtherList:
    myOtherFile.write(stuff + "\n")

myOtherFile.close()