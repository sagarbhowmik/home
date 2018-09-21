import re


def is_match(string):
    pattern = re.compile(r"(\w+)[@](\w+)[.]com")
    matched = pattern.match(string)
    if matched:
        userid = matched.group(1)
        domain = matched.group(2)
    return (userid, domain)




print is_match("sagarb12@gmail.com")