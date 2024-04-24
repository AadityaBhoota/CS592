def sum_to_n(n: int):
    return n * (n + 1) // 2

# Test the function with the provided examples
print(sum_to_n(30))  # Output should be 465
print(sum_to_n(100))  # Output should be 5050
print(sum_to_n(5))  # Output should be 15
print(sum_to_n(10))  # Output should be 55
print(sum_to_n(1))  # Output should be 1



METADATA = {}


def check(candidate):
    assert candidate(1) == 1
    assert candidate(6) == 21
    assert candidate(11) == 66
    assert candidate(30) == 465
    assert candidate(100) == 5050


check(sum_to_n)