import sys

if len(sys.argv) != 2:
    sys.exit("Missing argument: file name")

fname = sys.argv[1]

with open(fname, 'a') as f:
    f.write("Hello World!\n")
    for i in range(10):
        for j in range(10):
            f.write("%3d " % (i * j))
        f.write("\n")

