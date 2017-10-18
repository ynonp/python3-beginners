"""
Working with modules:
    import random
    from random import randint

    from random import *
    import random as rnd
"""
import checkIsraelID
import random as r

n = r.randint(0, 100)
print("Got: {}".format(n))

id = input("Please type in your ID number")
if checkIsraelID.checkID(id):
    print("Valid ID: {}".format(id))
else:
    print("Sorry, ID is not valid")
