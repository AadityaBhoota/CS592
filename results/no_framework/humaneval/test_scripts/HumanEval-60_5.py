def sum_to_n(n: int):
    return sum(range(1, n + 1))

# Testing the function
print(sum_to_n(30))  # 465
print(sum_to_n(100)) # 5050
print(sum_to_n(5))   # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))   # 1



METADATA = {}


def check(candidate):
    assert candidate(1) == 1
    assert candidate(6) == 21
    assert candidate(11) == 66
    assert candidate(30) == 465
    assert candidate(100) == 5050


check(sum_to_n)