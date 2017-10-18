while True:
    try:
        x = float(input("Please type a first number"))
        y = float(input("Please type a second number"))
        break
    except ValueError as e:
        print("Error. Please try again")
    except ZeroDivisionError as e:
        pass
    except Exception as e:
        pass

total = x + y
print("%f + %f = %f" % (x, y, total))
