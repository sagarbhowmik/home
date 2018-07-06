"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        x = math.log(num, 2)/math.log(4, 2)
        return x == int(x)


print Solution.isPowerOfFour(Solution(), 16777216)
print Solution.isPowerOfFour(Solution(), 5)
print Solution.isPowerOfFour(Solution(), 0)
print Solution.isPowerOfFour(Solution(), 1)
print Solution.isPowerOfFour(Solution(), 4194304)

print "-----------"
print math.log(4194304, 10)
print math.log(4, 10)
print math.log(4194304, 10)/math.log(4, 10)
print int(math.log(4194304, 10)/math.log(4, 10))
print math.log(4194304, 10)/math.log(4, 10) == int(math.log(4194304, 10)/math.log(4, 10))
