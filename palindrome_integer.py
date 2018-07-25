"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # quotient = temp_x = x
        # rev_x = 0
        # if x < 0:
        #     return False
        # if 0 < x < 10:
        #     return True
        # while quotient != 0:
        #     quotient = temp_x // 10
        #     remainder = temp_x % 10
        #     temp_x = quotient
        #     rev_x = rev_x * 10 + remainder * 10
        # if x == rev_x // 10:
        #     return True
        # else:
        #     return False
        if x < 0:
            return False
        if x < 10:
            return True
        str_int = str(x)
        for i in range(0, len(str_int)/2):
            if str_int[i] != str_int[len(str_int) - 1 - i]:
                return False
            else:
                continue
        return True


integer = 10
sol = Solution()
print(sol.isPalindrome(integer))

