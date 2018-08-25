def pythagorean_triplet(n, length):
    #sq_n = [int(i) ** 2 for i in n]
    #print sq_n
    n.sort
    for i in range(0, int(length)-2):
        for j in range(i + 1, int(length)-1):
            for k in range(j + 1, int(length)):
                if int(n[k]) ** 2 == int(n[i]) ** 2 + int(n[j]) ** 2:
                    return "Yes"
    return "No"


print pythagorean_triplet([86, 68, 17, 94, 5, 67, 54, 9, 24, 85, 93, 68, 49, 70, 31, 12, 15, 91, 28, 44, 5, 100, 75, 96, 7, 59, 90,
], 27)