def modp(n: int, p: int) -> int:
    return pow(2, n, p)

# Testing the function with the examples from the docstring
print(modp(3, 5))    # Output: 3
print(modp(1101, 101))    # Output: 2
print(modp(0, 101))    # Output: 1
print(modp(3, 11))    # Output: 8
print(modp(100, 101))    # Output: 1



METADATA = {}


def check(candidate):
    assert candidate(3, 5) == 3
    assert candidate(1101, 101) == 2
    assert candidate(0, 101) == 1
    assert candidate(3, 11) == 8
    assert candidate(100, 101) == 1
    assert candidate(30, 5) == 4
    assert candidate(31, 5) == 3


check(modp)