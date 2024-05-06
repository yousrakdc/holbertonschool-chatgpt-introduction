#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement `n` in each iteration
    return result  # Return the result

if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)
    
    # Convert the first argument to an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a non-negative integer")
        sys.exit(1)
    
    # Ensure the input is non-negative
    if n < 0:
        print("Error: Please provide a non-negative integer")
        sys.exit(1)

    # Calculate the factorial
    f = factorial(n)
    print(f)