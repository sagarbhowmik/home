import re

pattern = re.compile(r"abc\sxyz")

# If zero or more characters at the beginning of string match the regular expression pattern,
# return a corresponding MatchObject instance.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.
if pattern.match("xabc xyzd"):
    print("match match")

# Scan through string looking for the first location where the regular expression pattern produces a match, and
# return a corresponding MatchObject instance.
# Return None if no position in the string matches the pattern;
# note that this is different from finding a zero-length match at some point in the string.
elif pattern.search("sdxy"):
    print("search match")
else:
    print("not match")


# Example:
import re
pattern = re.compile(r"\[(on|off)\]") # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example


# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com", "45454"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)