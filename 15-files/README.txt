Working with files:

1. Writing text to files:
    with open(filename, 'w') as f:
        f.write("Hello World!\n")


2. Reading text from files:
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')


