def first_Digit(n):
    while n >= 10:
        n //= 10
    return n

# Test the function




def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)