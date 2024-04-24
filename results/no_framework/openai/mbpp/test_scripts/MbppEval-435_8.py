def last_digit(n):
    return n % 10

# Test the function




def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0

check(last_Digit)