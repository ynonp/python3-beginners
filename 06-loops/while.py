"""
Python Loops:
    while
    for
"""

name = input("Who are you?")
while len(name) < 10:
    print("Name too short. Please try again")
    name = input("Who are you?")

print("Welcome, %s" % name)
