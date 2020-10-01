"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
# Initialize loop
while True:
    # Tokenize a string
    input_string = input("Enter your equation: ")
    tokens = input_string.split(' ')
    result = None

    operator = tokens[0]
    if operator == "q":
        break
