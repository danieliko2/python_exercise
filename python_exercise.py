import sys
import logging

def main():
    parameters = sys.argv

    # input validation - only 1 numeric argument
    if len(parameters) == 1:
        print("Error: No input")
        exit(1)
    if len(parameters) != 2:
        print("Error: Please provide only 1 input")
        exit(1)
    if not parameters[1].isnumeric():
        print("Error: Parameter is not a number")
        exit(1)

    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    num=int(parameters[1])
    print("arg: ", num)

    for i in range(1, num):
        if num % i == 0:
            print(i)


if __name__ == '__main__':
    main()