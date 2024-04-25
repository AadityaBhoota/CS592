import math

def is_polite(n):
    def count_divisors(number):
        count = 0
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                if number / i == i:
                    count += 1
                else:
                    count += 2
        return count

    polite_count = 0
    current_number = 1

    while True:
        if count_divisors(current_number) == n:
            polite_count += 1
            if polite_count == n:
                return current_number
        current_number += 1

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)