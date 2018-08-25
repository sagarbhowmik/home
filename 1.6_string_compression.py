def stringCompression(string):
    return_string = []
    count = 1
    previous = string[0]
    for each in string[1:]:
        if previous == each:
            count += 1
        else:
            return_string.append(previous)
            return_string.append(str(count))
            previous = each
            count = 1
    return_string.append(previous)
    return_string.append(str(count))
    print return_string
    if len(string) <= len(return_string):
        return string
    else:
        return ''.join(return_string)


print stringCompression("aabcccccaaa")