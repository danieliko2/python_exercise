import sys

num = sys.argv[1]
if len(sys.argv) == 1:
    print("no input")

if num.isnumeric():
    print("num")
else:
    print("not a number")
print("arg: ", sys.argv[1])

