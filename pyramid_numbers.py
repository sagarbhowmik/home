"""
Given a pyramid of consecutive integers:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
......

Find the sum of all the integers in the row number N.
For example:
The row #3: 4 + 5 + 6 = 15
The row #5: 11 + 12 + 13 + 14 + 15 = 65
"""
def sum_pyramid_numbers(row):
    i = 1
    last_number = 0
    while i <= row:
        for n in range(i):
           last_number += 1
        i += 1
    print last_number
    sum = last_number
    while row != 1:
        last_number -= 1
        sum += last_number
        row -= 1
    print sum


sum_pyramid_numbers(100)