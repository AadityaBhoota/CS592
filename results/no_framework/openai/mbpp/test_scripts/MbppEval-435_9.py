def last_Digit(n):
    return n % 10

# Test the function with examples
assert last_Digit(123) == 3
assert last_Digit(25) == 5
assert last_Digit(30) == 0



def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0

check(last_Digit)