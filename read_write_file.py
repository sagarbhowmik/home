def write_to_file(x, filename="list_contents.txt"):
    """
    Writes each element in the list to a new line to a text file
    :param x: List of strings
    :param filename: File name where user wants to write, default list_contents.txt
    :return: void
    """
    with open(filename, "w") as file_handle:
        for each_element in x:
            file_handle.write(each_element+"\n")

def read_from_file(filename="list_contents.txt"):
    """
    :param filename: File name where user wants to read from, default list_contents.txt
    :return: List of items from the file
    """
    with open(filename) as file_handle:
        content_list = file_handle.read().splitlines()
    return content_list

x = ["table", "chair", "cup", "fork", "sagar"]
#write_to_file(x, "test.txt")

print read_from_file("test.txt")