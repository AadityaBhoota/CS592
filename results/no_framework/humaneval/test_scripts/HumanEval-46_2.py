def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2

    fib_nums = [0, 0, 2, 0]  # Initialize the sequence with the first four elements

    for i in range(3, n):
        current_sum = sum(fib_nums)
        fib_nums = [fib_nums[1], fib_nums[2], fib_nums[3], current_sum]

    return fib_nums[-1]

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