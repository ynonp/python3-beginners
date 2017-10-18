import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    sys.exit("Missing required argument: name")

print("Hello: {}".format(name))

