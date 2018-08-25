def find_nth_element(n):
    """
    Returns the n'th element of the sequence 2, 1, 3, 4, 7, 11, 18,...
    :param n: integer input
    :return: integer or error if input is < 1
    """
    nth_element_dict = {}
    if n < 1:
        return "Error: Please enter valid input greater than 0"
    nth_element_dict[1] = 2
    nth_element_dict[2] = 1
    for i in range(3, n+1):
        nth_element_dict[i] = nth_element_dict[i - 1] + nth_element_dict[i - 2]
    return nth_element_dict[n]


print find_nth_element(100)