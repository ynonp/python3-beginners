# Printing 50 times I Love Python is a bit harder than
# printing 5. You won't write 50 print statements in code.
# Instead we'll use a loop

# Here the iteration variable is named _
# That's a python convention that means we don't care
# about its value.
for _ in range(50):
    print("I Love Python")

# Had we wanted to use the iteration number inside the
# loop (for example to print a counter next to our text)
# we would give it a meaningful name. For example:

for counter in range(50):
    print("I love Python - %d times" % counter)

# Note the counter starts at 0 and iterates until 49,
# that's one less than the number we passed to range.
