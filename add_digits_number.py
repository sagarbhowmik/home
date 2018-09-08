"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        while num > 9:
            ret += num % 10
            num /= 10
        ret = ret + num
        if ret < 10:
            return ret
        else:
            return self.addDigits(ret)



print Solution.addDigits(Solution(),708538619)