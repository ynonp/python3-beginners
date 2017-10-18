# A function is defined by the keyword def
# Our task is to write a function that gets two numbers,
# so we write their names in parenthesis after the function name
def sum_numbers_in_range(start, end):
    # Inside the function, start and end are treated
    # like variables but their value was already provided
    # by the calling code

    # As this function calculates a sum of numbers,
    # we can use the following loop
    total = 0
    for num in range(start, end):
        total += num

    # After the loop is done and we've found the value,
    # we use return to "return" it to the calling code
    return total

# Outside the function we define a new variable called
# mysum. Note that we could have used the name "total" just
# as well, because variables defined in a function do not
# conflict with variables defined outside.

# mysum will take the value passed to return in line 17
# by the function
# Writing the function name with values in parenthesis like
# the following line "calls" the function passing 2 as the
# value of "start" and 10 as the value of "end"
mysum = sum_numbers_in_range(2, 10)

print("Sum was:", mysum)
