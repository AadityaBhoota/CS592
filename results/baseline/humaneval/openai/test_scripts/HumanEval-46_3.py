def fib4(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    fib_nums = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib_sum = fib_nums[3] + fib_nums[2] + fib_nums[1] + fib_nums[0]
        fib_nums[0] = fib_nums[1]
        fib_nums[1] = fib_nums[2]
        fib_nums[2] = fib_nums[3]
        fib_nums[3] = fib_sum

    return fib_nums[3]

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)