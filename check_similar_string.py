def check_one_edit(string_one, string_two):
    if len(string_one) != len(string_two) and abs(len(string_one) - len(string_two)) != 1:
        return False
    length = ""
    strike = 0
    count = len(string_one) if len(string_one) >= len(string_two) else len(string_two)
    if len(string_one) == len(string_two):
        length = "equal"
    elif len(string_one) > len(string_two):
        length = "large_one"
    else:
        length = "large_two"
    for i in range(count-1):
        if string_one[i] == string_two[i]:
            continue
        else:
            strike += 1
        if strike == 1:
            if length == "equal" and string_one[i+1: count] == string_two[i+1: count]:
                return True
            elif length == "large_one" and string_one[i+1: count] == string_two[i:count]:
                return True
            elif length == "large_two" and string_one[i: count] == string_two[i+1:count]:
                return True
            else:
                return False
    return True

print check_one_edit("pale", "pale")