def uniqueString(input):
    print len(input)
    for each in input:
        print each
    string_set = set()
    for each_char in input:
        if each_char not in string_set:
            string_set.add(each_char)
        else:
            return False
    return True

print uniqueString("dfdfd")
