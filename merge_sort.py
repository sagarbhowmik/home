def merge(list_a, list_b):
    merge_list = []
    while len(list_a) != 0 and len(list_b) != 0:
        if list_a[0] < list_b[0]:
            merge_list.append(list_a[0])
            list_a.remove(list_a[0])
        else:
            merge_list.append(list_b[0])
            list_b.remove(list_b[0])
    if len(list_a) == 0:
        merge_list += list_b
    else:
        merge_list += list_a
    return merge_list


def merge_sort(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    else:
        mid = len(input_list)/2
        part_one = merge_sort(input_list[:mid])
        part_two = merge_sort(input_list[mid:])
        return merge(part_one, part_two)


print merge_sort([4, 56, 2, -1, 45454])
