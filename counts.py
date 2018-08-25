def bin_search(array, n):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) / 2
        if array[mid] <= n:
            low = mid + 1
        else:
            high = mid - 1
    return high


def counts(nums, maxes):
    answer = []
    count = 0
    nums.sort()
    print nums
    for each_max in maxes:
        answer.append(bin_search(nums, each_max) + 1)

    return answer


print counts([1,4,6,2,3,3,5,5,9], [3,5])