try:
    x = float(input("Please type a first number"))
    y = float(input("Please type a second number"))
    total = x + y
    print("%f + %f = %f" % (x, y, total))
except ValueError as e:
    print("Error: ", e)
