def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2

    fib_list = [0, 0, 2, 0]  # Starting values for n=0, n=1, n=2, n=3

    for i in range(4, n+1):
        next_val = fib_list[i-1] + fib_list[i-2] + fib_list[i-3] + fib_list[i-4]
        fib_list.append(next_val)

    return fib_list[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)