def UniqueCharString(string_input):
    my_dict = {}
    for char in string_input:
        if char == " ":
            continue
        elif char not in my_dict.keys():
            my_dict[char] = 1
        else:
            return False
    return True


print UniqueCharString("cat")
print UniqueCharString("apple")
print UniqueCharString("quick dg jmp ver lazy fox")
