import math


def is_prime(n):
    """
    Returns whether a number is prime or not
    :param n: integer input
    :return: bool True/False
    """
    if n <= 0 or n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:  # checks if n is even, 2 is only even prime number
        return False
    else:
        prime = False
        for i in range(3, n + 1, 2):
            if n % i == 0:
                if not prime:
                    prime = True
                else:
                    return False
        return prime


print is_prime(13)

