#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer representing the number
                 for which the factorial will be calculated.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Convert command-line argument to integer
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
