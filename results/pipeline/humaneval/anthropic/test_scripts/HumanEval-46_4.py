def fib4(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    fib4_list = [0, 0, 2, 0]  # Initialize the first four elements

    if n < 4:
        return fib4_list[n]

    for i in range(4, n + 1):
        fib4_list.append(fib4_list[i - 1] + fib4_list[i - 2] + fib4_list[i - 3] + fib4_list[i - 4])

    return fib4_list[n]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)