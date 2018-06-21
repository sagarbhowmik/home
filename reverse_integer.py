"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−2^31,  2^31 − 1].

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_str = str(x)
        if x_str[0] == '-':
            negative = True
            rev_x = [s for s in x_str[1:]]
        else:
            negative = False
            rev_x = [s for s in x_str]
        for i in range(0,len(rev_x)//2):
            t = rev_x[i]
            rev_x[i] = rev_x[len(rev_x)-i-1]
            rev_x[len(rev_x)-i-1] = t

        rev_x_str = ''.join(rev_x)
        rev_x_int = int(rev_x_str)
        if negative:
            rev_x_int *= -1
        if rev_x_int < -2 ** 31 or rev_x_int > 2 ** 31:
            return 0
        return rev_x_int


integer = 1534236469
sol = Solution()
print(sol.reverse(integer))

