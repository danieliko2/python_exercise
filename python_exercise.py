import sys

num = sys.argv[1]

# input validation - only 1 numeric argument
if len(sys.argv) == 1:
    print("Error: No input")
    exit(1)
if len(sys.argv) != 2:
    print("Error: Please provide only 1 input")
    exit(1)
if not num.isnumeric():
    print("Error: Parameter is not a number")
    exit(1)

num=int(num)
print("arg: ", num)

for i in range(1, num):
    if num % i == 0:
        print(i)