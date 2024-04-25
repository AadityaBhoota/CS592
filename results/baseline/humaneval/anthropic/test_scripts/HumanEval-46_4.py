def fib4(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2

    fib4_arr = [0, 0, 2]
    for i in range(3, n+1):
        fib4_i = fib4_arr[i-1] + fib4_arr[i-2] + fib4_arr[i-3]
        fib4_arr.append(fib4_i)

    return fib4_arr[n]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)