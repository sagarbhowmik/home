def divide(dividend, divisor):
    count = 0
    neg_div = False
    if divisor < 0:
        neg_div = True
        divisor = abs(divisor)
    if dividend < 0:
        neg_div = False if neg_div else True
        dividend = abs(dividend)
    if divisor == 1:
        return min(dividend,2147483647) if not neg_div else max(-dividend, -2147483648)
    if dividend - divisor == 0:
        count = 1
    while dividend - divisor > 0:
        if dividend - divisor > 0:
            count += 1
            dividend -= divisor
    if neg_div:
        return max(-count, -2147483648)
    else:
        return min(count, 2147483647)


print divide(2147483647, 2)