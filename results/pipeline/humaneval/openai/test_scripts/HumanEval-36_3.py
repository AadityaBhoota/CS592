def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    
    def contains_digit_7(number: int) -> bool:
        return '7' in str(number)

    count = 0
    for num in range(1, n):
        if num % 11 == 0 or num % 13 == 0:
            if contains_digit_7(num):
                count += 1

    return count



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