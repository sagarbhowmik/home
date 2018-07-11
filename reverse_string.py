def reverse_string(str):
    str_list = list(str)
    print str
    j = len(str) - 1
    for i in range(len(str)/2):
        temp = str_list[i]
        str_list[i] = str_list[j]
        str_list[j] = temp
        j -= 1
    print ''.join(str_list)



reverse_string("ab")