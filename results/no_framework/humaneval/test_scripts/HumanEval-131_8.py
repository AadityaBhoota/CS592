def digits(n):
    product = 1
    has_odd_digit = False
    
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            has_odd_digit = True
        n //= 10
    
    return product if has_odd_digit else 0

# Test cases
print(digits(1))    # 1
print(digits(4))    # 0
print(digits(235))  # 15

def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2468) == 0


check(digits)