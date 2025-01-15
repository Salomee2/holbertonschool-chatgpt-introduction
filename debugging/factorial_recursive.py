#!/usr/bin/python3
import sys

# Function: factorial
# Description:
# This function computes the factorial of a given integer n.
# It uses a recursive approach, where the factorial of a number n is defined as:
# n! = n * (n-1) * (n-2) * ... * 1, and factorial(0) = 1 by definition.

# Parameters:
#   n (int): The integer for which the factorial is to be calculated.

# Returns:
#   int: The factorial of the number n.
#         If n is 0, the function returns 1 (base case).
#         Otherwise, it recursively multiplies n by the factorial of (n-1).

def factorial(n):
    if n == 0:
        return 1  # Base case: factorial(0) is 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

# Getting the number from command line argument
f = factorial(int(sys.argv[1]))

# Printing the result of the factorial calculation
print(f)

