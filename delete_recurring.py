
def delete_recurring(string):
    string_set = set()
    string_ret = ""
    for char in string:
        if char not in string_set:
            string_set.add(char)
            string_ret += char
    return string_ret


string = "aabbdfdfndfdfdfadddddacc"
print(delete_recurring(string))


