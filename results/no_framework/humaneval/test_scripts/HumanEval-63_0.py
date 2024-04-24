def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        fib_list = [0, 1, 1]
        for i in range(3, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2] + fib_list[i-3])
        return fib_list[n]

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927


check(fibfib)