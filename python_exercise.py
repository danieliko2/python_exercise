import sys
import logging
import os

def main():
    parameters = sys.argv

    # input validation - only 1 numeric argument
    if len(parameters) == 1:
        file_path = os.path.expanduser("~") + "/python_exercise_input.txt"
        with open(file_path, 'r') as file:
            num = file.read().rstrip()

    elif len(parameters) != 2:
        print("Error: Please provide only 1 input")
        exit(1)

    elif not parameters[1].isnumeric():
        print("Error: Parameter is not a number")
        exit(1)

    else:
        num=int(parameters[1])

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='/var/log/python_exercise.log', level=logging.INFO)
    print(num)
    for i in range(1, num):
        if num % i == 0:
            logging.info(i)
            print(i)


if __name__ == '__main__':
    main()