def fib(n: int):
    if n <= 0:
        return "Invalid input. n should be a positive integer."

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1, 1]
        for i in range(3, n+1):
            fib_number = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(fib_number)
        return fib_sequence[n]

# Testing the function
if __name__ == "__main__":
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    print("All tests passed!")



METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)