def fizz_buzz(n: int):
    def count_sevens(num):
        return str(num).count('7')

    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_sevens(i)

    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3



METADATA = {}


def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026


check(fizz_buzz)