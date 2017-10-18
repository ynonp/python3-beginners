# Write a function that takes a number
# and returns the sum of its digits

def sum_digits(number):
    # To calculate sum of digits we can use math
    # A number modulus 10 returns the right-most digit
    # And a number divided by 10 returns the remaining digits
    # without the rightmost one
    total = 0
    while number > 0:
        right_digit = number % 10
        total += right_digit

        # The special // in python is called integer
        # division. It divides and truncates all digits after
        # the floating point leaving us with an integer value
        number = number // 10

    return total

print(sum_digits(1234))
