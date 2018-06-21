"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = 0
        max_length = []
        substring = ""  # type: str
        i = 0
        j = 0
        while i != len(s):
            if substring.find(s[i]) < 0:
                substring += s[i]
                i += 1
            else:
                j += 1
                length = len(substring)
                max_length.append(length)
                substring = s[j]
                i = j + 1
        if not max_length or len(substring) > max(max_length):
            return len(substring)
        return max(max_length)


string1 = "abcabcbb"
string2 = "bbbbb"
string3 = "pwwkew"
string4 = "abcdefghijklmnopqrstuvwxyz"
string5 = "aab"
string6 = "dvdf"
string7 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdef..."

sol = Solution()
print(sol.lengthOfLongestSubstring(string1))
print(sol.lengthOfLongestSubstring(string2))
print(sol.lengthOfLongestSubstring(string3))
print(sol.lengthOfLongestSubstring(string4))
print(sol.lengthOfLongestSubstring(string5))
print(sol.lengthOfLongestSubstring(string6))
print(sol.lengthOfLongestSubstring(string7))
