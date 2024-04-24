def even_odd_count(num):
    even_count = 0
    odd_count = 0

    # Get the absolute value of the number to handle negative numbers
    num = abs(num)

    # Convert the number to a string to iterate over its digits
    num_str = str(num)

    # Count the number of even and odd digits
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)

# Test cases
print(even_odd_count(-12))  # Should return (1, 1)
print(even_odd_count(123))  # Should return (1, 2)

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