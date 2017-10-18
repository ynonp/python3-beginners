# input reads a value from the user
# saving it in a variable named age
age = input("How old are you? ")

# age is now a text string, so we can't
# check if it's smaller than 18. They're of different types.
# Instead we need to tell python to treat age
# as a number by wrapping it in int(...)
if int(age) < 18:
    print("Too young to vote")
else:
    print("You may vote")
