def minimumBribes(q):
    sorted_q = sorted(q)
    bribe = 0
    for i in range(0, len(q)):
        if abs(q[i]-sorted_q[i]) > 2:
            return "Chaotic"
        elif abs(q[i]-sorted_q[i]) >= 1:
            bribe += 1
    return (bribe+1)/2

print minimumBribes([2,1,5,3,4])
print minimumBribes([2,5,1,3,4])
print minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])
print minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])