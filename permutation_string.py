def permutation_string(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    if string_one == string_two:
        return True
    dict_one, dict_two = {}, {}
    for i in range(len(string_one)):
        if string_one[i] not in dict_one.keys():
            dict_one[string_one[i]] = 1
        else:
            dict_one[string_one[i]] = int(dict_one[string_one[i]]) + 1
        if string_two[i] not in dict_two.keys():
            dict_two[string_two[i]] = 1
        else:
            dict_two[string_two[i]] = int(dict_two[string_two[i]]) + 1
    for k,v in dict_one.items():
        try:
            if v != dict_two[k]:
                return False
        except KeyError:
            return False
    return True


print permutation_string("abc", "dsa")