import math

def last_Digit_Factorial(n):
    factorial_result = math.factorial(n)
    last_digit = factorial_result % 10
    return last_digit

def check(candidate):
    assert last_Digit_Factorial(4) == 4
    assert last_Digit_Factorial(21) == 0
    assert last_Digit_Factorial(30) == 0

check(last_Digit_Factorial)