def quick_sort(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    else:
        pivot = input_list[0]
        i = 0
        for j in range(len(input_list) - 1):
            if input_list[j+1] < pivot:
                temp = input_list[j+1]
                input_list[j+1] = input_list[i+1]
                input_list[i+1] = temp
                i += 1
        temp = input_list[0]
        input_list[0] = input_list[i]
        input_list[i] = temp
        part_one = quick_sort(input_list[:i])
        part_two = quick_sort(input_list[i+1:])
        part_one.append(input_list[i])
        return part_one + part_two

print quick_sort([4, 56, 2, -1, 45454])