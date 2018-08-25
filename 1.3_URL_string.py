def URLify(string, true_length):
    URLString = []
    string.strip()
    for each in string[:true_length]:
        if each == " ":
            URLString.append("%20")
        else:
            URLString.append(each)
    return "".join(URLString)


print URLify("Mr John Smith      ", 13)
string = "Mr John Smith      "
print string[:13]