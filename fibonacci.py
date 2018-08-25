def get_fibonacci(n):
    a, b = 0, 1
    a_new, b_new = 0, 1
    fib, fib_new = [], [a_new, b_new]
    for i in range(n - 2):
        fib.append(a)
        fib_new.append(fib_new[i] + fib_new[i+1])
        a, b = b, a + b
    print(fib)
    print(fib_new)


get_fibonacci(10)