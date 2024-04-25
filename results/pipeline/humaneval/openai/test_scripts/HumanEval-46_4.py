def fib4(n: int):
    # Step 1: Initialize the list to store the first 4 elements of the Fib4 sequence
    fib4_list = [0, 0, 2, 0]

    # Step 2: Loop to compute the next elements of the Fib4 sequence
    for i in range(4, n + 1):
        fib4_next = fib4_list[i-1] + fib4_list[i-2] + fib4_list[i-3] + fib4_list[i-4]
        fib4_list.append(fib4_next)

    # Step 3: Return the n-th element of the Fib4 sequence
    return fib4_list[n]

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)