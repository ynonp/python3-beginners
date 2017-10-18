"""
Python Loops:
    while
    for
"""

while True:
    name = input("Who are you?")
    if len(name) >= 10: break

    print("Name too short. Please try again")

print("Welcome, %s" % name)
