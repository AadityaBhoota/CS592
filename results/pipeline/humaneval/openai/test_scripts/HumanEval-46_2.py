def fib4(n: int):
    if n < 4:
        return 0
    else:
        fib4_sequence = [0, 0, 2, 0]  # Initial sequence

        for i in range(4, n+1):
            next_element = fib4_sequence[-1] + fib4_sequence[-2] + fib4_sequence[-3] + fib4_sequence[-4]
            fib4_sequence = fib4_sequence[1:] + [next_element]

        return fib4_sequence[-1]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)