def modp(n: int, p: int) -> int:
    result = 1
    base = 2
    n = n % (p-1)  # reduce n to smaller number to avoid overflow in exponentiation
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n // 2
    return result

# Testing the function
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