a = "This is a string"
# Print from 1st index to end
print(a[1:])
# Print from start to index 6 (not including 6)
print(a[:6])
# Print from start to finish every 2
print(a[::2])
# Use negative to start from the end
print(a[:-2])
print(a[::-2])
# Easily reverse a string
print(a[::-1])
b = a[::-1]
print(b)