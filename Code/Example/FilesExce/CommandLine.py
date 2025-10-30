import sys

if len(sys.argv) != 2:
    print("A file name must be provided as a command line", \
          "argument.")
    quit()

inf = open(sys.argv[1], "r")

total = 0

line = inf.readline()
while line != "":
    total = total + float(line)
    line = inf.readline()

inf.close()

print("The total of the values in", sys.argv[1], "is", total)