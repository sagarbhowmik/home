def sum_bits(n):
    """
    Returns the sum of bits of a number
    :param n: Integer number
    :return: Integer
    """
    bin_string = bin(n)
    count = 0
    for i in range(2, len(bin_string)):
        if bin_string[i] == str(1):
            count += 1
    return count


print sum_bits(7)