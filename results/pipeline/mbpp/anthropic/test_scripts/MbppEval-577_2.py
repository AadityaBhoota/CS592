def last_Digit_Factorial(n):
    last_digit_cycle = [1, 2, 6, 4]
    return last_digit_cycle[n % 4]

def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)