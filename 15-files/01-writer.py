import sys

if len(sys.argv) != 2:
    sys.exit("Missing argument: file name")

fname = sys.argv[1]

with open(fname, 'w') as f:
    f.write("Hello World!\n")
