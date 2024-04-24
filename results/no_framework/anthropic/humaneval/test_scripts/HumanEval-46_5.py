def fib4(n: int) -> int:
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib4_seq = [0, 0, 2, 0]
    for i in range(4, n + 1):
        next_fib4 = sum(fib4_seq)
        fib4_seq.pop(0)
        fib4_seq.append(next_fib4)

    return fib4_seq[-1]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)