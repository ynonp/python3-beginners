# this program prints its own code
with open(__file__, 'r') as fr:
    for line in fr:
        print(line, end="")
