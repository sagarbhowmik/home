"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0][0] if strs[0] != "" else ""
        ret = []
        append = True
        r = ""
        for i in range(0, min(len(s) for s in strs)):
            for j in range(len(strs)-1):
                if j == 0 and strs[j][i] != strs[j+1][i]:
                    return ''.join(ret) if len(ret) > 0 else ""
                elif strs[j][i] == strs[j+1][i]:
                    r = strs[j][i]
                else:
                    append = False
            if not append:
                return ''.join(ret) if len(ret) > 0 else ""
            else:
                 ret.append(r)
        return ''.join(ret)


l1 = ["flower", "flow", "flight"]
l2 = ["dog", "racecar", "car"]
l3 = []
l4 = ["a"]
l5 = [""]
l6 = ["aa", "ab"]
sol = Solution()
print("l1: {}".format(sol.longestCommonPrefix(l1)))
print("l2: {}".format(sol.longestCommonPrefix(l2)))
print("l3: {}".format(sol.longestCommonPrefix(l3)))
print("l4: {}".format(sol.longestCommonPrefix(l4)))
print("l5: {}".format(sol.longestCommonPrefix(l5)))
print("l6: {}".format(sol.longestCommonPrefix(l6)))


