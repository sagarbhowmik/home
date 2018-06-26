"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        if len(s) == 2:
            if s[0] == '(' and s[1] == ')':
                return True
            elif s[0] == '[' and s[1] == ']':
                return True
            elif s[0] == '{' and s[1] == '}':
                return True
            else:
                return False

        bracket_type_dict = {
            '(': "round_open",
            ')': "round_close",
            '{': "curly_open",
            '}': "curly_close",
            '[': "square_open",
            ']': "square_close"}
        next_close = []
        if bracket_type_dict[s[0]] == "round_close" or bracket_type_dict[s[0]] == "curly_close" or bracket_type_dict[
            s[0]] == "square_close":
            return False
        for each in s:
            bracket_type = bracket_type_dict[each]
            if bracket_type == "round_open" or bracket_type == "curly_open" or bracket_type == "square_open":
                next_close.append(bracket_type)
                continue
            if (bracket_type == "round_close" and next_close[-1] != "round_open") or (
                    bracket_type == "curly_close" and next_close[-1] != "curly_open") or (
                    bracket_type == "square_close" and next_close[-1] != "square_open"):
                return False
            else:
                next_close.pop()
        return True if not next_close else False


string1 = ""
string2 = "()"
string3 = "()[]{}"
string4 = "(]"
string5 = "{[]}"
string6 = "{[}"
string7 = "([)]"
string8 = ")}{({))[{{[}"
string9 = "(()])}[}[}[]][}}[}{})][[(]({])])}}(])){)((){"
sol = Solution()
print("string1", ":", sol.isValid(string1))
print("string2", ":", sol.isValid(string2))
print("string3", ":", sol.isValid(string3))
print("string4", ":", sol.isValid(string4))
print("string5", ":", sol.isValid(string5))
print("string6", ":", sol.isValid(string6))
print("string7", ":", sol.isValid(string7))
print("string8", ":", sol.isValid(string8))
print("string9", ":", sol.isValid(string9))
