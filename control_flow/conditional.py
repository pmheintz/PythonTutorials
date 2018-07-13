"""
Conditional logic
"""

if 100 > 10:
    print("100 is greater than 10")

print("Python uses indentation for code blocks")

value = "Yellow"
if value == "Green":
    print("Go")
if value == "Red":
    print("Stop")

print("*" * 20)
if value == "Green":
    print("Go")
elif value == "Yellow":
    print("Prepare to stop")
else:
    print("Stop")
