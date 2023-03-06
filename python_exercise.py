import sys

num = sys.argv[1]
if len(sys.argv) == 1:
    print("no input")
    exit(1)
if len(sys.argv) != 2:
    print("please provide only 1 input")
    exit(1)
if num.isnumeric():
    print("num")
else:
    print("not a number")
    exit(1)

print("arg: ", sys.argv[1])

