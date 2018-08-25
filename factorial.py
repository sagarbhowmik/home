import math


def find_factorial(n):
    """
    Returns the factorial of a given number (n!)
    :param n: integer input
    :return: integer or error if n is negative
    """
    if n < 0:
        return "Error: enter positive integer"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1)


print find_factorial(256)
print math.factorial(256)