def even_odd_count(num):
    num = abs(num)
    even_count = sum(1 for digit in str(num) if int(digit) % 2 == 0)
    odd_count = sum(1 for digit in str(num) if int(digit) % 2 != 0)
    return (even_count, odd_count)

# Test cases
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)

def check(candidate):

    # Check some simple cases
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)
    assert candidate(-2) == (1, 0)
    assert candidate(-45347) == (2, 3)
    assert candidate(0) == (1, 0)


    # Check some edge cases that are easy to work out by hand.
    assert True


check(even_odd_count)