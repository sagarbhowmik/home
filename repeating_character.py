# Complete the firstRepeatingLetter function below.
def firstRepeatingLetter(s):
    dict_s = {}
    first_letter = False
    for each_char in s:
        if each_char not in dict_s.keys():
            dict_s[each_char] = 1
        else:
            dict_s[each_char] = int(dict_s[each_char]) + 1
    print dict_s
    ret = ""
    for k,v in dict_s.iteritems():
        if v > 1:
            if ret == "":
                ret = k
            elif s.find(k) < s.find(ret):
                ret = k
            else:
                continue
    return ret

print firstRepeatingLetter("bacab")