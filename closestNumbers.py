def closestNumbers(numbers):
    sorted_numbers = sorted(numbers)
    print  sorted_numbers
    min_diff, diff = 0, 0
    diff_dict = {}
    for i in range(0, len(numbers)-1):
        j = i + 1
        diff = abs(sorted_numbers[i] - sorted_numbers[j])
        diff_dict[sorted_numbers[i]] = sorted_numbers[j]
        if min_diff == 0:
            min_diff = diff
        else:
            min_diff = min(diff, min_diff)
    sorted_number_pairs = []
    for k, v in diff_dict.iteritems():
        if abs(int(k) - int(v)) == min_diff:
            sorted_number_pairs.append(k)
            sorted_number_pairs.append(v)
    sorted_number_pairs.sort()

    for i in range(0, len(sorted_number_pairs) - 1, 2):
        print sorted_number_pairs[i] ,
        print sorted_number_pairs[i + 1]



closestNumbers([4, -2, -1, 3])