#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    # Convert the first argument to an integer and handle potential errors
    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("The input must be a non-negative integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Calculate and print the factorial
    f = factorial(n)
    print(f)
