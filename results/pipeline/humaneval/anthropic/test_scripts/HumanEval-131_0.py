def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    if product == 1:
        return 0
    else:
        return product

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