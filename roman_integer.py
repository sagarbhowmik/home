"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

roman_value = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_num = 0  # type: int
        last_c = None
        subtract = False
        # print(roman_value)
        for c in s:
            if ((last_c == 'I' and (c == 'V' or c == 'X')) or
                    (last_c == 'X' and (c == 'L' or c == 'C')) or
                    (last_c == 'C' and (c == 'D' or c == 'M'))):
                subtract = True
            if subtract:
                int_num -= roman_value[last_c]
                special_value = roman_value[c] - roman_value[last_c]
                int_num += special_value
                subtract = False
            else:
                int_num += roman_value[c]
            last_c = c
        return int_num


s1 = "III"
s2 = "IV"
s3 = "IX"
s4 = "LVIII"
s5 = "MCMXCIV"

sol = Solution()
print(sol.romanToInt(s1))
print(sol.romanToInt(s2))
print(sol.romanToInt(s3))
print(sol.romanToInt(s4))
print(sol.romanToInt(s5))
