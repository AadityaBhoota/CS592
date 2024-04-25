def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fibfib_list = [0, 0, 1]
    for i in range(3, n+1):
        fibfib_list.append(sum(fibfib_list[-3:]))
    return fibfib_list[n]



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