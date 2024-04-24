def fib4(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0
    elif n == 3:
        return 0

    fib4_list = [0, 0, 2, 0]
    for i in range(4, n + 1):
        next_fib4 = sum(fib4_list)
        fib4_list = fib4_list[1:] + [next_fib4]

    return fib4_list[-1]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)