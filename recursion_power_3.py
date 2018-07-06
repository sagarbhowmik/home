"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        """
        Not so good surprisingly passed all submissions
        def multipleOfThree(n):
            if n == 1:
                return True
            if n%3 is not 0:
                return False
            if n/3 == 1:
                if n%3 == 0:
                    return True
                else:
                    return False
            else:
                return multipleOfThree(n/3)

        return False if n == 0 else multipleOfThree(n)
        """

        #another solution but seems slower
        if n == 1:
            return True
        if n == 0:
            return False
        if n%3 != 0:
            return False
        return self.isPowerOfThree(n/3)


print Solution.isPowerOfThree(Solution(), 27)
print Solution.isPowerOfThree(Solution(), 0)
print Solution.isPowerOfThree(Solution(), 9)
print Solution.isPowerOfThree(Solution(), 45)
print Solution.isPowerOfThree(Solution(), 1)
print Solution.isPowerOfThree(Solution(), 19682)
