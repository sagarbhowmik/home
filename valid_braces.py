# Complete the braces function below.
def braces(values):
    valid_braces = []
    for each_value in values:
        if each_value == "":
            valid_braces.append("YES")
            continue
        if len(each_value) % 2 != 0:
            valid_braces.append("NO")
            continue
        if len(each_value) == 2:
            if each_value[0] == "(" and each_value[1] == ")":
                valid_braces.append("YES")
                continue
            elif each_value[0] == "[" and each_value[1] == "]":
                valid_braces.append("YES")
                continue
            elif each_value[0] == "{" and each_value[1] == "}":
                valid_braces.append("YES")
                continue
            else:
                valid_braces.append("NO")
                continue
        next_close = []
        if each_value[0] == ")" or each_value[0] == "]" or each_value[0] == "}":
            valid_braces.append("NO")
            continue
        for each_char in each_value:
            if each_char == "(" or each_char == "[" or each_char == "{":
                next_close.append(each_char)
                continue
            if (each_char == ")" and next_close[-1] != "(") or (each_char == "]" and next_close[-1] != "[") or (
                    each_char == "}" and next_close[-1] != "{"):
                valid_braces.append("NO")
                break
            else:
                next_close.pop()
        if not next_close:
            valid_braces.append("YES")

    return valid_braces





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # values_count = int(t())

    values = ["{[}]"]

    # for _ in xrange(values_count):
    #     values_item = t()
    #     values.append(values_item)

    print braces(values)
