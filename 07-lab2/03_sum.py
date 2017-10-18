# There are several ways here so I'll present 3
#
# 1. Using Step
# To find all the even numbers between 2 and 100
# we'll use a for loop.
#
# Range can take start, end and step values,
# which makes it easy to print and sum all
# numbers in range
# 
# As you probably remember, range
# iterates until one less than the number specified.
# So to reach 100 we need to pass it the value 101.
# This next loop prints all the numbers between 2 and 100
# inclusive:
for num in range(2,101,2):
    print(num)

# To sum them we should create a variable that'll hold
# the sum, and add each number to it.
# Python provides a shortcut for that operation:
# total += number
# is the short way to tell python:
# total = total + number
# or in English - add the value from variable number to the 
# variable total

total = 0
for num in range(2,101,2):
    total += num


print("1. Total sum is:", total)

# 2. Using Range
# Alternatively we can use a standard for loop
# and perform the calculation inside the loop body:

total = 0
for num in range(51):
    total += num * 2

print("2. Total sum is:", total)

# 3. Using Math
# And as a third option, we also know that the even numbers
# is an arithmetic progression so we can use simple math
total = (100+2) * 50/2
print("3. Total sum is:", total)
