# First print 3 numbers
# (I just made them up, you can select any numbers you want)
print("First number: 10")
print("Second number: 15")
print("Third number: 12")

# Now ask the user which one is the largest,
# saving their guess in a new variable called guess
guess = input("Which one is the largest? ")

# Finally let's see if they got it right
if guess == "15":
    print("Bravo!")

# Notice how "15" is quoted. This means its a text string.
# When comparing things in python it's important to compare things
# of the same type.
# Since input(...) returns text, so we need to compare that with
# the text a user should type, and text is always written in quotes.

